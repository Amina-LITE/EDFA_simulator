import numpy as np
import pandas as pd
from scipy.interpolate import interp1d
import matplotlib.pyplot as plt
from glob import glob
from os.path import join, split, isdir
from Settings import * 



def Get_Excel_file(gff_type): 
    GFF_PATH = r'GFFs'
    Excel_file_path = join(GFF_PATH, gff_type+'.xlsx')
    data = pd.read_excel(Excel_file_path,sheet_name='Insertion_Loss')
    return data 
    
#data = Get_Excel_file('GFF2')

def Load_GFF_data(WL_sig, WL_pump, WL_ase,gff_type):
    #file = r"gff\GFF2.xlsx"   # Will be remplaced by Get_Excel_file: data = Get_Excel_file(GFF2)
    data =  Get_Excel_file(gff_type)# pd.read_excel(file,sheet_name='Insertion_Loss')
    Wavelength  = np.squeeze( data[['Wavelength']] )
    Loss = np.squeeze(data[['IL']] )
    Loss_interpolation = interp1d(Wavelength, Loss, kind='linear', fill_value="extrapolate")
    Loss_sig_raw =  Loss_interpolation(WL_sig)
    Loss_pump_raw =  Loss_interpolation(WL_pump)
    Loss_ase_raw =  Loss_interpolation(WL_ase)

    # Put zero all the entries that are not availible in the excel sheet
    Loss_sig=[0]*len(WL_sig)
    Loss_pump=[0]*len(WL_pump)
    Loss_ase=[0]*len(WL_ase)

    for i in range(len(Wavelength)) :#this solution works but its a O(N^2) so I can make it more efficient if its too so 
        for j in range (len(WL_sig)):
            if int(Wavelength[i])==int(WL_sig[j]):#did the int stuff to avoid situation where both are doubles that are the same with diffrent decimal values
                Loss_sig[j]=Loss_sig_raw[i]
                break
            if int(Wavelength[i])>int(WL_sig[len(WL_sig)-1]):
                break
        for j in range (len(WL_pump)):
            if int(Wavelength[i])==int(WL_pump[j]):#did the int stuff to avoid situation where both are doubles that are the same with diffrent decimal values
                Loss_pump[j]=Loss_pump_raw[i]
                break
            if int(Wavelength[i])>int(WL_pump[len(WL_pump)-1]):
                break
        for j in range (len(WL_ase)):
            if int(Wavelength[i])==int(WL_ase[j]):#did the int stuff to avoid situation where both are doubles that are the same with diffrent decimal values
                Loss_ase[j]=Loss_ase_raw[i]
                break
            if int(Wavelength[i])>int(WL_ase[len(WL_ase)-1]):
                break
           

a = Load_GFF_data(WL_sig, WL_pump, WL_ase,'GFF2') 