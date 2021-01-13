import numpy as np
import pandas as pd
import Settings as settings
import new_amp as ap
import database as db
from datetime import date

def lossReport():
    #Reading the amp discription and adding each of the different sections to a data frame
    beforeAmpCheck=True
    listOfDF=[]
    listofTotalIL=[]
    i=0
    signaltoEDFCheck=True
    curEDF=0
    while i< len(ap.OpticalComponent):# This loop creates all the dataFrames that will be added to excel
        tempTotalIL=0
        if beforeAmpCheck==True :
            tempList=[]
            while ap.OpticalComponent[i][0]!="iso":#creates the first dataframe for components before amp
                loss=getInsertionLoss(ap.OpticalComponent[i][0],ap.OpticalComponent[i][2])
                tempDic={'Component': ap.OpticalComponent[i][0], 'Name': ap.OpticalComponent[i][1], 'Type': ap.OpticalComponent[i][2], 'Mean IL': loss }
                i+=1
                tempTotalIL+=loss
                tempList.append(tempDic)

            df = pd.DataFrame(tempList,columns=tempDic.keys())
            df.name = "Before Amplifer"          
            listOfDF.append(df)
            listofTotalIL.append(tempTotalIL)
            beforeAmpCheck=False
        else: #creates data frames for all components after first dataframe for before amp
            tempList=[]
            while ap.OpticalComponent[i-1][0]!="edf" and i< len(ap.OpticalComponent) :
                loss=getInsertionLoss(ap.OpticalComponent[i][0],ap.OpticalComponent[i][2])
                tempDic={'Component': ap.OpticalComponent[i][0], 'Name': ap.OpticalComponent[i][1], 'Type': ap.OpticalComponent[i][2], 'Mean IL': loss }
                i+=1
                tempTotalIL+=loss
                tempList.append(tempDic)
                

            df = pd.DataFrame(tempList,columns=tempDic.keys())
            i+=1     
            if signaltoEDFCheck==True:#adding the various titles of the tables to their respective dataframes
                df.name = "Amplifer Input - EDF1"
            elif i< len(ap.OpticalComponent):
                df.name = "EDF"+str(curEDF)+" - EDF"+str(curEDF+1)
            else:
                df.name = "EDF"+str(curEDF)+" - Connector Out"
            curEDF+=1
            signaltoEDFCheck=False
            listofTotalIL.append(tempTotalIL)
            listOfDF.append(df)
    #entering the dataframes to excel
    writer = pd.ExcelWriter('C:\\Users\\cha78317\\Box\\EDFA simulator\\edfasim Oct 2020\\Reports\\LossReports\\LossReport.xlsx',engine='xlsxwriter')
    workbook=writer.book
    worksheet=workbook.add_worksheet('Result')
    writer.sheets['Result'] = worksheet

    cell_format = workbook.add_format()
    cell_format.set_align('center')
    worksheet.write_string(0, 0, "Loss Report ", cell_format)
    worksheet.write_string(0, 1, str(date.today()), cell_format)
    

    sheetRow=3#keeps track of current row
    title_format = workbook.add_format() #format for title cells 
    title_format.set_font_size(20)
    worksheet.write_string(sheetRow, 0, listOfDF[0].name,title_format)
    sheetRow+=1
    for i in range(len(listOfDF)):#going through dataframe and adding the dataframes to excel
        listOfDF[i].to_excel(writer,sheet_name='Result',startrow=sheetRow , startcol=0)
        if i<len(listOfDF)-1:
            worksheet.write_string(listOfDF[i].shape[0] + sheetRow+3, 0, listOfDF[i+1].name,title_format)
        sheetRow+=listOfDF[i].shape[0]
        worksheet.write_string(sheetRow+1, 0, "Total Insertion Loss", cell_format)
        worksheet.write_string(sheetRow+1, 1, str(listofTotalIL[i]), cell_format)
        sheetRow+=4
    #formatting cells
    worksheet.set_column('A:A', 20)
    worksheet.set_column('B:B', 20)
    worksheet.set_column('C:C', 20)
    worksheet.set_column('D:D', 20)
    worksheet.set_column('E:E', 20)
    writer.save()


def getInsertionLoss (cFamily,cType):
    # getting loss values for each component
    query_str = 'ComponentFamily == "' + cFamily + '" and ComponentType == "' + cType + '"'
    data = db.excel_db().run_excel_query(query_str)
    cLoss     = data["Loss"].item()
    return cLoss



lossReport()
