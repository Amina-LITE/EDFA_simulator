import numpy as np
import pandas as pd
import Settings as settings
from scipy.interpolate import interp1d
import matplotlib.pyplot as plt
from glob import glob
from os.path import join, split, isdir




def Get_Excel_file(gff_type): 
    GFF_PATH = r'GFFs'
    Excel_file_path = join(GFF_PATH, gff_type+'.xlsx')
    data = pd.read_excel(Excel_file_path,sheet_name='Insertion_Loss')
    return data 
    
#data = Get_Excel_file('GFF2')
def closest_index(WL_list, K): 
    Closest = WL_list[min(range(len(WL_list)), key = lambda i: abs(WL_list[i]-K))] 
    return list(WL_list).index(Closest)

def Put_zeros(Loss_list, index, direction):#adds zeros to the wavelength that dont have a defined value in the GFF
    if direction == "start": 
        i = 0 
        while i < index+1: 
            Loss_list[i]= 0 
            i += 1    
    if direction == "end": 
        i = len(Loss_list)-1 
        while i > index-2: 
            Loss_list[i]= 0 
            i -= 1      
    return Loss_list

def Load_GFF_data(WL_sig, WL_pump, WL_ase,gff_type):#lods the gff data from the excel file 
    #file = r"gff\GFF2.xlsx"   # Will be remplaced by Get_Excel_file: data = Get_Excel_file(GFF2)
    data =  Get_Excel_file(gff_type)# pd.read_excel(file,sheet_name='Insertion_Loss')
    Wavelength  = np.squeeze( data[['Wavelength']] )
    Loss = np.squeeze(data[['IL']] )
    Loss_interpolation = interp1d(Wavelength, Loss, kind='linear', fill_value="extrapolate")
    Loss_sig_raw =  Loss_interpolation(WL_sig)
    Loss_pump =  Loss_interpolation(WL_pump)
    Loss_ase_raw =  Loss_interpolation(WL_ase)

    closest_index_ase_start = closest_index(WL_ase,Wavelength[0])
    closest_index_ase_end = closest_index(WL_ase,Wavelength[len(Wavelength)-1])
    closest_index_sig_start = closest_index(WL_sig,Wavelength[0])
    closest_index_sig_end = closest_index(WL_sig,Wavelength[len(Wavelength)-1])

    Loss_ase = Put_zeros(Loss_ase_raw, closest_index_ase_start, "start")
    Loss_ase = Put_zeros(Loss_ase, closest_index_ase_end, "end")
    Loss_sig = Put_zeros(Loss_sig_raw, closest_index_sig_start, "start")
    Loss_sig = Put_zeros(Loss_sig, closest_index_sig_end, "end")  
    Loss_pump[0] = 0 
    
    Total_loss = np.concatenate((Loss_sig,Loss_pump,Loss_ase))
    return Total_loss
'''
    ####### REMMMMMMMMMMMMMMMMMMMMMMMMMMMOVVVVVVVVVVVVVVVVVVE THHHHHHHHHHHHHHIIIIIIS LATER
    wavelist= np.concatenate((WL_sig,WL_pump,WL_ase))
    plt.plot(wavelist[:settings.N_sig] , Loss_sig,color="green")#green should be same as red at end
    plt.plot(wavelist[settings.N_ase:] , Loss_ase,color="blue")
    plt.plot(data[['Wavelength']] , data[['IL']],color="red")
    plt.grid()
    plt.show()
    '''
    

#a = Load_GFF_data(WL_sig, WL_pump, WL_ase,'GFF2') 

