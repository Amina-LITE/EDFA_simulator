import boto3
import time
import os
import re
import sys
from datetime import datetime
import dbconfig

athena_s3_bucket = dbconfig.athena_s3_bucket
aws_region = dbconfig.aws_region

## Set your access and secret key values here
aws_access_key_id = dbconfig.aws_access_key_id
aws_secret_access_key = dbconfig.aws_secret_access_key
##
##

#====================================================
# S3 Methods wrapped in class
#====================================================
class S3:
    def __init__(self, aws_access_key_id, aws_secret_access_key, aws_region="us-west-2"):
        self.s3Client = boto3.client('s3', region_name=aws_region,
            aws_access_key_id=aws_access_key_id,
            aws_secret_access_key=aws_secret_access_key)

        self.s3Res = boto3.resource('s3', region_name=aws_region,
            aws_access_key_id=aws_access_key_id,
            aws_secret_access_key=aws_secret_access_key)

    #====================================================
    # Get object from s3
    #====================================================
    def s3_get_object(self, SrcBucket, SrcKey):
        fileobj = self.s3Client.get_object(Bucket=SrcBucket, Key=SrcKey)
        return fileobj

#====================================================
# Athena Methods wrapped in class
#====================================================
class Athena:
    def __init__(self, aws_access_key_id, aws_secret_access_key, aws_region="us-west-2"):
        self.athenaClient = boto3.client('athena', region_name=aws_region,
            aws_access_key_id=aws_access_key_id,
            aws_secret_access_key=aws_secret_access_key)

    #====================================================
    # Poll Athena Query Status
    #====================================================
    def poll_query_status(self, _id):
        state  = 'RUNNING'
        while state == 'RUNNING' or state == 'QUEUED':
            result = self.athenaClient.get_query_execution( QueryExecutionId = _id )
            if 'QueryExecution' in result and 'Status' in result['QueryExecution'] and 'State' in result['QueryExecution']['Status']:
                state = result['QueryExecution']['Status']['State']
                if state == 'FAILED':
                    return result
                elif state == 'SUCCEEDED':
                    return result
                elif state == 'RUNNING':
                    time.sleep(2)
                elif state == 'QUEUED':
                    time.sleep(1)
                else:
                    raise Exception(f"Encountered unknown state in athena poll query: {state}")

    #====================================================
    # Run Athena Query with Polling
    #====================================================
    def run_athena_query(self, query, log=False, s3_output=athena_s3_bucket, response_req=False):
        try:
            if log:
                print("-----------------------------------------------------------------------")
                print(query)
            response = self.athenaClient.start_query_execution(
                QueryString=query,
                ResultConfiguration={
                    'OutputLocation': "s3://" + s3_output},
                WorkGroup="primary")

            QueryExecutionId = response['QueryExecutionId']
            result = self.poll_query_status(QueryExecutionId)

            if result['QueryExecution']['Status']['State'] == 'SUCCEEDED':
                if log:
                    print("Query SUCCEEDED: {}".format(QueryExecutionId))
                    print("Time Taken (millisec) : " + str(result['QueryExecution']['Statistics']['EngineExecutionTimeInMillis']))
                    print("Data Scanned (bytes)  : " + str(result['QueryExecution']['Statistics']['DataScannedInBytes']))
                    print("-----------------------------------------------------------------------")
                if response_req:
                    s3_path = result['QueryExecution']['ResultConfiguration']['OutputLocation']
                    filename = re.findall(r'.*\/(.*)', s3_path)[0]
                    return filename
                else:
                    return True
            else:
                print(result['QueryExecution']['Status']['StateChangeReason'])
                if log:
                    print("Query " + result['QueryExecution']['Status']['State'] + ": {}".format(QueryExecutionId))
                    print("Time Taken (millisec) : " + str(result['QueryExecution']['Statistics']['EngineExecutionTimeInMillis']))
                    print("Data Scanned (bytes)  : " + str(result['QueryExecution']['Statistics']['DataScannedInBytes']))
                    print("-----------------------------------------------------------------------")
                return False
        except Exception as e:
            print("SQL Query execution failed. Check logs for more details")
            exc_type, _, exc_tb = sys.exc_info()
            print(exc_type, exc_tb.tb_lineno, e)
            return False


athena_obj = Athena(aws_access_key_id, aws_secret_access_key)
s3_obj = S3(aws_access_key_id, aws_secret_access_key)

## Set the query you want to fireclear
athena_query = "select * from cktpack.tbl_wdm"
##

def run_query(query_str, log):
# if log True it will print query execution metadata
# if response is exepected e.g (select query) the set response_req = True 
# it will return filename where response is stored in athena_s3_bucket (default)
# if query fails it will return False
    athena_output_filename = athena_obj.run_athena_query(query_str, log, response_req=True)
    if athena_output_filename:
        readobj = s3_obj.s3_get_object(athena_s3_bucket, athena_output_filename)
        ddl_string = readobj['Body'].read().decode('utf-8-sig')
        # now = datetime.now()
        # filename = now.strftime("%d%m%Y-%H-%M-%S") + ".csv"
        # filepath = os.path.join('queries', filename)
        # file = open(file, "x") 
        # file.write(ddl_string) 
        # file.close()
        print(ddl_string)
        return ddl_string
    else:
        print("Query execution failed")
        return False

run_query(athena_query, False)
