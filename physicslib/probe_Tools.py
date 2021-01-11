import numpy as np
import pandas as pd
import Settings as settings
from os.path import join, split, isdir
from scipy.interpolate import interp1d
import new_amp as ap

def Get_Probe_values(Probe_name, amp): 

    Probe_Type, Power_p1, Power_p2 = Get_Probe_Spectrum(Probe_name, amp)
    if Probe_Type == 'Gain': 
        probe_values = gainProbe(Power_p1, Power_p2)
    if Probe_Type == 'PDSig': 
        probe_values = sigPowerProbe(Power_p1) 
    if Probe_Type == 'PDASE': 
        probe_values = sigPowerProbe(Power_p1,2) 
    elif Probe_Type == 'NF': 
        probe_values = noiseFigureProbe(Power_p1, Power_p2)
    
    return probe_values

def Get_Probe_Spectrum(Probe_name, amp): 
    #From Probe name, get  'Port1_Component_Name' ,  'Port2_Component_Name'
    #From Port_component name, get index for amp 
    # From amp[index], get output forward 
    #p1 refers to port 1, p2 refers to port 2 
    
    PD_dict = dict((x[2], x[0:]) for x in ap.OpticalProbe)
    cmps = ap.OpticalComponent
    if Probe_name in PD_dict: 
        #Port 1 
        c_p1 = PD_dict.get(Probe_name)[3]
        try:        
            result_p1 = [element for element in cmps if element[1] == c_p1]
            index_p1 = cmps.index(result_p1[0]) + 1 
        except: 
            index_p1 = 0     

        Port_1_sig = amp[index_p1]
        Power_p1 = Port_1_sig.getOutputForward()

        #Port 2 
        Power_p2 = []
        c_p2 = PD_dict.get(Probe_name)[4]   
        if c_p2 != '' : 
            result_p2 = [element for element in cmps if element[1] == c_p2]
            index_p2 = cmps.index(result_p2[0]) + 1 
            Port_2_sig = amp[index_p2]
            Power_p2 = Port_2_sig.getOutputForward()
        elif  c_p2 == '' : 
            split_out = Port_1_sig.getTapOutput()
            split_ratio = Port_1_sig.getSplitRatio2()
            Power_p1 = split_out*split_ratio # Need to check correct ratio and opration (unit?)
    else: 
        print('Probe not defined')    
    Probe_Type = PD_dict.get(Probe_name)[0]
    return Probe_Type, Power_p1, Power_p2

def arrayRemover(sigListTemp,pumpListTemp,aseListTemp):
    sigList=[]
    pumpList=[]
    aseList=[]
    for i in range ((max(settings.N_sig,settings.N_ase))):
        if i < settings.N_sig:
            sigList.append(sigListTemp[i][0])
        if i < settings.N_ase:
            aseList.append(aseListTemp[i][0])
        if i <settings.N_pump-1:
            pumpList.append(pumpListTemp[i][0])
    
    return sigList,pumpList,aseList


def listSplitter(concatList,concatList2=[],numList=1):#issues occuring because list holding signals have each data point in an array
    sigListTemp=concatList[0:settings.N_sig]#issue occurs only for these three not the wavs
    pumpListTemp=concatList[settings.N_sig:settings.N_pump]#issues are in the NF function and the power if outuput signal is used
    aseListTemp=concatList[settings.N_sig+settings.N_pump:]
    
    if isinstance(sigListTemp[0], np.ndarray): 
        sigList,pumpList,aseList=arrayRemover(sigListTemp,pumpListTemp,aseListTemp)
    else:
        sigList,pumpList,aseList=sigListTemp,pumpListTemp,aseListTemp
    
    sigWavList=settings.WL[0:settings.N_sig]
    pumpWavList=settings.WL[settings.N_sig:settings.N_pump]
    aseWaveList=settings.WL[settings.N_sig+settings.N_pump:]

    if numList==2:
        sigListTemp2=concatList2[0:settings.N_sig]
        pumpListTemp2=concatList2[settings.N_sig:settings.N_pump]
        aseListTemp2=concatList2[settings.N_sig+settings.N_pump:]

        if isinstance(sigListTemp2[0], np.ndarray): 
            sigList2,pumpList2,aseList2=arrayRemover(sigListTemp2,pumpListTemp2,aseListTemp2)
        else:
             sigList2,pumpList2,aseList2=sigListTemp2,pumpListTemp2,aseListTemp2

        return sigList,pumpList,aseList,sigList2,pumpList2,aseList2,sigWavList,pumpWavList,aseWaveList

    return sigList,pumpList,aseList,sigWavList,pumpWavList,aseWaveList


#total power is the sum of each list 
def sigPowerProbe(concatList,sigType=0):
    if sigType==0:#signal
        tempList=listSplitter(concatList)
        signalList=tempList[0]
        signalWaveList=tempList[3]
        signalTotalPower=sum(signalList)
        return signalList,signalWaveList,signalTotalPower
    elif sigType==1:#pump
        tempList=listSplitter(concatList)
        pumpList=tempList[1]
        pumpWaveList=tempList[4]
        pumpTotalPower=sum(pumpList)
        return pumpList,pumpWaveList,pumpTotalPower
    else:#ase
        tempList=listSplitter(concatList)
        aseList=tempList[2]
        aseWaveList=tempList[5]
        aseTotalPower=sum(aseList)
        return aseList,aseWaveList,aseTotalPower


def gainProbe (concatList,concat2,sigType=0):
    if sigType==0:  #signal gain
        tempList=listSplitter(concatList,concat2,2)
        probeSigList1=tempList[0]
        probeSigList2=tempList[3]
        sigWaveList=tempList[6]
        sigGainList=[]

        for i in range(len(probeSigList1)):
            sigGainList.append(probeSigList2[i]/probeSigList1[i])

        return sigGainList, sigWaveList

    elif sigType==1:  #pump gain
        tempList=listSplitter(concatList,concat2,2)
        probePumpList1=tempList[1]
        probePumpList2=tempList[4]
        pumpWaveList=tempList[7]
        pumpGainList=[]

        for i in range(len(probePumpList1)):
            pumpGainList.append(probePumpList2[i]/probePumpList1[i])

        return pumpGainList, pumpWaveList
    else:  #ase gain
        tempList=listSplitter(concatList,concat2,2)
        probeAseList1=tempList[2]
        probeAseList2=tempList[5]
        aseWaveList=tempList[8]
        aseGainList=[]

        for i in range(len(probeAseList1)):
            aseGainList.append(probeAseList2[i]/probeAseList1[i])

        return aseGainList, aseWaveList


def noiseFigureProbe(inputSignal,outputSignal) :#not tested 
    tempList=listSplitter(inputSignal,outputSignal,2)
    WL_sig=tempList[6]
    WL_ase=tempList[8]
    inASE=tempList[2]
    outASE=tempList[5] 
    

    hp = 6.62607004e-34 # Planck constant m2kg/s
    c  = 299792458      # Speed of light in vacuum m/s
    
    N_sig = settings.N_sig
    N_ase = settings.N_ase

    GainSig      =  gainProbe(inputSignal,outputSignal)[0]

    NU_sig       = c/(WL_sig*1e-9)    # Sig grid Frquency array  # Delta nu array @ Sig wavelebgth for NF calulation. 
    DNU_sig      = np.full((N_sig), 0.00)
    DNU_sig[0]   = NU_sig[0]-NU_sig[1]
    DNU_sig[1:]  = -np.diff(NU_sig)   
    
    NU_ase    = c/(WL_ase*1e-9)    # ASE grid Frquency array
    # Delta nu array for ASE calulation. It is only calculated at ASE Wavelengths
    DNU_ase = np.full((N_ase), 0.00)
    DNU_ase[0] = NU_ase[0]-NU_ase[1]
    DNU_ase[1:] = -np.diff(NU_ase)

    PASE_in  = inASE/DNU_ase      # W/Hz  
    PASE_out = outASE/DNU_ase     # W/Hz 
    PASE_in_interp  = interp1d(WL_ase, PASE_in,  kind='linear')   # W/Hz
    PASE_out_interp = interp1d(WL_ase, PASE_out, kind='linear')   # W/Hz
    PASE_in_SigGrid    = PASE_in_interp(WL_sig)      # W/Hz
    PASE_out_SigGrid   = PASE_out_interp(WL_sig)     # W/Hz
    PASE_in_SigGrid    = PASE_in_SigGrid *DNU_sig    # Within Signal bandwidth
    PASE_out_SigGrid   = PASE_out_SigGrid*DNU_sig    # Within Signal bandwidth
    # NF = Pase_added / Gsig*h*v*dv + 1 / Gsig        
    gainhnudeltanu = hp*np.multiply(np.multiply(GainSig,DNU_sig),NU_sig) 
    PASE_added_SigGrid = PASE_out_SigGrid - PASE_in_SigGrid*GainSig
    NF = PASE_added_SigGrid/gainhnudeltanu + np.reciprocal(GainSig) 
    #nf should be a list 
    return NF,WL_sig,gainhnudeltanu

