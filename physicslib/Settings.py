import numpy as np
##############################################################
## Describe source

"""Signal""" 
N_sig    = 100
P_sig_dBm = 0    # dBm
P_sig    = np.power(10,-(30-P_sig_dBm)/10) # W 
P_sig_ch = P_sig/N_sig
WL_sig_start = 1528 #nm
WL_sig_stop  = 1567   #nm

WL_sig   = np.linspace(WL_sig_start, WL_sig_stop, N_sig)
Signalf  = P_sig/N_sig * np.full((N_sig,1), 1)
Signalb  = P_sig/N_sig * np.full((N_sig,1), 0)

"""Pump""" 
N_pump   = 1
#P_pump multiple values for multiple values
P_pump = {"pump1": 500e-3,"pump2": 1000e-3,"pump3": 1000e-3}
#P_pump   = 500e-3 # W 
WL_pump  = np.linspace(974, 974, N_pump)
# Pumpf    = P_pump/N_pump * np.full((N_pump,1), 0)
# Pumpb    = P_pump/N_pump * np.full((N_pump,1), 0)
Pumpf    = 0/N_pump * np.full((N_pump,1), 0)
Pumpb    = 0/N_pump * np.full((N_pump,1), 0)

"""ASE""" 
N_ase   = 11
P_ase   = 0e-8 # W 
WL_ase  = np.linspace(1500, 1650, N_ase)
ASEf    = P_ase/N_ase * np.full((N_ase,1), 1)
ASEb    = P_ase/N_ase * np.full((N_ase,1), 1)

WL    = np.concatenate((WL_sig, WL_pump, WL_ase), axis=0) # duplicate power array to account for backward propagating power10
Power = np.concatenate((Signalf, Pumpf, ASEf), axis=0)  

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
""" Constants """
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
NS    = 5             # Number of sections considered
#Len and Temp_sim multiple values for multiple edfs
edf_properties = {"EDF1":{"Len":5, "Temp_sim":65},"EDF2":{"Len":5, "Temp_sim":65},"EDF3":{"Len":40, "Temp_sim":65},"EDF4":{"Len":5, "Temp_sim":65}}
# Len   = 12             # EDF length in meters
# Temp_sim = 22
