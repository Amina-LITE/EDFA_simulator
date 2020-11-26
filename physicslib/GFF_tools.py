import numpy as np
import pandas as pd
from scipy.interpolate import interp1d
import matplotlib.pyplot as plt


def Get_Excel_file(gff_type): 
    # Will create the excel filename based on the gff_type and load the correct file from the GFF folder. (Amina)

def Load_GFF_data(WL_sig, WL_pump, WL_ase):
    file = r"gff\GFF2.xlsx"   # Will be remplaced by Get_Excel_file
    data = pd.read_excel(file,sheet_name='Loss')
    Wavelength  = np.squeeze( data[['Wavelength']] )
    Loss = np.squeeze(data[['Loss']] )
    Loss_interpolation = interp1d(Wavelength, Loss, kind='linear')
    # Put zero all the entries that are not availible in the excel sheet. (Aidan)
    Loss_sig