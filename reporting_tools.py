import numpy as np
import pandas as pd
import Settings as settings
import new_amp as ap

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
            while ap.OpticalComponent[i][0]!="iso":
                tempDic={'Component': ap.OpticalComponent[i][0], 'Name': ap.OpticalComponent[i][1], 'Type': ap.OpticalComponent[i][2], 'Mean IL': 50 }
                #the il is wrong atm
                i+=1
                tempTotalIL+=50#FIX THIS ITS NOT 50 ITS WHAT EVER I DO IN THE ABOVE LINE
                tempList.append(tempDic)

            df = pd.DataFrame(tempList,columns=tempDic.keys())
            df.name = "Before Amplifer"          
            listOfDF.append(df)
            listofTotalIL.append(tempTotalIL)
            beforeAmpCheck=False
        else: 
            tempList=[]
            while ap.OpticalComponent[i-1][0]!="edf" and i< len(ap.OpticalComponent) :
                tempDic={'Component': ap.OpticalComponent[i][0], 'Name': ap.OpticalComponent[i][1], 'Type': ap.OpticalComponent[i][2], 'Mean IL': 50 }
                #the il is wrong atm
                i+=1
                tempTotalIL+=50#FIX THIS ITS NOT 50 ITS WHAT EVER I DO IN THE ABOVE LINE
                tempList.append(tempDic)
                

            df = pd.DataFrame(tempList,columns=tempDic.keys())
            i+=1     
            if signaltoEDFCheck==True:
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
    writer = pd.ExcelWriter('C:\\Users\\cha78317\\Documents\\test.xlsx',engine='xlsxwriter')
    workbook=writer.book
    worksheet=workbook.add_worksheet('Result')
    writer.sheets['Result'] = worksheet
    worksheet.write_string(0, 0, "Loss Report ")
    worksheet.write_string(0, 1, "Fix this to show date ")# need to add date

    sheetRow=3
    worksheet.write_string(sheetRow, 0, listOfDF[0].name)
    sheetRow+=1
    for i in range(len(listOfDF)):
        listOfDF[i].to_excel(writer,sheet_name='Result',startrow=sheetRow , startcol=0)
        if i<len(listOfDF)-1:
            worksheet.write_string(listOfDF[i].shape[0] + sheetRow+3, 0, listOfDF[i+1].name)
        sheetRow+=listOfDF[i].shape[0]
        worksheet.write_string(sheetRow+1, 0, "Total Insertion Loss")
        worksheet.write_string(sheetRow+1, 1, str(listofTotalIL[i]))
        sheetRow+=4
    writer.save()



    #https://datascience.stackexchange.com/questions/46437/how-to-write-multiple-data-frames-in-an-excel-sheet
    #Use this link to figure out adding to excel spreadsheet

    

lossReport()

