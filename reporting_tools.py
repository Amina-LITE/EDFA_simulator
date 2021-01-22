import numpy as np
import pandas as pd
import Settings as settings
import new_amp as ap
import database as db
from datetime import date
from scipy.stats import linregress

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
            tempTotalIL="{:10.4f}".format(tempTotalIL)
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
    
    sheetRow=1#keeps track of current row
    #format for cells 
    title_format = workbook.add_format({ 
        'fg_color': '#5DADE2',
        'font_color': '#000000',
        'align': 'center',
        'border': 1})
    total_format = workbook.add_format({ 
        'fg_color': '#F2D218',
        'font_color': '#000000',
        'align': 'center',
        'bold': 1})
    title_format.set_font_size(20)
    total_format.set_font_size(12)
    worksheet.write_string(0, 0, "Loss Report ", total_format)
    worksheet.write_string(0, 1, str(date.today()), total_format)
    sheetRow+=2

    worksheet.merge_range('A'+str(sheetRow)+':E'+str(sheetRow), listOfDF[0].name, title_format)
    for i in range(len(listOfDF)):#going through dataframe and adding the dataframes to excel
        listOfDF[i].to_excel(writer,sheet_name='Result',startrow=sheetRow , startcol=0)
        if i<len(listOfDF)-1:
            worksheet.merge_range('A'+str(listOfDF[i].shape[0] + sheetRow+4)+':E'+str(listOfDF[i].shape[0] + sheetRow+4), listOfDF[i+1].name, title_format)
        sheetRow+=listOfDF[i].shape[0]
        worksheet.merge_range('A'+str(sheetRow+2)+':D'+str(sheetRow+2), "Total Insertion Loss", total_format)
        worksheet.write_string(sheetRow+1, 4, str(listofTotalIL[i]), total_format)
        sheetRow+=3
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




def probeReport(probeList): 
    writer = pd.ExcelWriter('C:\\Users\\cha78317\\Box\\EDFA simulator\\edfasim Oct 2020\\Reports\\ProbeReports\\ProbeReport.xlsx',engine='xlsxwriter')
    workbook=writer.book
    title_format = workbook.add_format({ 
        'fg_color': '#5DADE2',
        'font_color': '#000000',
        'align': 'center',
        'border': 1})
    title2_format = workbook.add_format({ 
        'fg_color': '#F2D218',
        'font_color': '#000000',
        'align': 'center',
        'bold': 1})
    title_format.set_font_size(12)
    for i,probe in enumerate(probeList):
        dataList=probe[0]
        waveList=probe[1]
        probeName=ap.OpticalProbe[i][2]
        probeType=ap.OpticalProbe[i][0]
        worksheet=workbook.add_worksheet(probeName)
        writer.sheets[probeName] = worksheet
        worksheet.write_string(0, 0, probeName+" Report ", title_format)
        worksheet.write_string(0, 1, str(date.today()), title_format)
        
        worksheet.write_string(2, 0, "Wavelength", title2_format)
        worksheet.write_string(2, 1, probeType+ "(dB)", title2_format)
        
        dbData=[] #used for calculation of ripple

        for i in range(len(dataList)):
            worksheet.write(i+3, 0, waveList[i])#wavelength
            if dataList[i]==0:
                dbValue=0    
            else:
                dbValue= 10*np.log10(dataList[i])#value be it gain nf etc
            worksheet.write(i+3, 1,dbValue)
            dbData.append(dbValue)
        
        if probeType!="PDASE" and probeType!="PDSig":#within this if ripple and tilt is calculated 
            worksheet.write_string(2, 2, "Ripple (dB)", title2_format)
            slope, intercept, r_value, p_value, stderr = linregress(waveList, dbData)
            tilt=calcTilt(waveList[0],waveList[-1],slope,intercept)
            for i in range(len(waveList)):
                linRegressValue=slope*waveList[i] + intercept
                ripple=dbData[i] - linRegressValue
                worksheet.write(i+3, 2,ripple)
            worksheet.write_string(2, 3, "Tilt", title2_format)
            worksheet.write_string(3, 3, str(tilt))
        else:#displays the total power
            worksheet.write_string(2, 2, "Total Power", title2_format)
            if dataList[i]==0:
                dbTotalPower=0    
            else:
                dbTotalPower=10*np.log10(probe[2])
            
            worksheet.write_string(3, 2, str(dbTotalPower))

        worksheet.set_column('A:A', 20)
        worksheet.set_column('B:B', 20)
        worksheet.set_column('C:C', 20)
        worksheet.set_column('D:D', 20)

        
        chart = workbook.add_chart({'type': 'scatter'})
        chart.add_series({
            'categories': '='+probeName+'!$A$4:$A$'+str(len(dataList)+4),
            'values':     '='+probeName+'!$B$4:$B$'+str(len(dataList)+4),
            'trendline': {
                'type': 'linear',
                'name': 'Linear Trend',
                'line': {
                    'color': 'red',
                    'width': 1,
                    'dash_type': 'long_dash',
                },
            },
        })
        #creating the axis titles and graph title
        chart.set_x_axis({
            'name': 'Wavelength (nm)',
            'name_font': {'size': 14, 'bold': True},
            'num_font':  {'italic': True },
        })

        chart.set_y_axis({
            'name': probeType+'( dB)',
            'name_font': {'size': 14, 'bold': True},
            'num_font':  {'italic': True },
        })

        chart.set_title({'name': probeName})
        worksheet.insert_chart('F2', chart)

    writer.save()



def calcTilt(firstWav,lastWav,slope,intercept):
    firstVal=slope*firstWav + intercept
    lastVal=slope*lastWav + intercept

    return lastVal-firstVal

