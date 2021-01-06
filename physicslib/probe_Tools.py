import numpy as np
import pandas as pd
import Settings as settings
from os.path import join, split, isdir
from scipy.interpolate import interp1d


def listSplitter(concatList,concatList2=None):
    sigList=concatList[0:settings.N_sig]
    pumpList=concatList[settings.N_sig:settings.N_pump]
    aseList=concatList[settings.N_sig+settings.N_pump:]

    sigWavList=settings.WL[0:settings.N_sig]
    pumpWavList=settings.WL[settings.N_sig:settings.N_pump]
    aseWaveList=settings.WL[settings.N_sig+settings.N_pump:]

    if concatList2!=None:
        sigList2=concatList2[0:settings.N_sig]
        pumpList2=concatList2[settings.N_sig:settings.N_pump]
        aseList2=concatList2[settings.N_sig+settings.N_pump:]
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
        tempList=listSplitter(concatList,concat2)
        probeSigList1=tempList[0]
        probeSigList2=tempList=[3]
        sigWaveList=tempList[6]
        sigGainList=[]

        for i in range(len(probeSigList1)):
            sigGainList.append(probeSigList2[i]/probeSigList1[i])

        return sigGainList, sigWaveList
    elif sigType==1:  #pump gain
        tempList=listSplitter(concatList,concat2)
        probePumpList1=tempList[1]
        probePumpList2=tempList=[4]
        pumpWaveList=tempList[7]
        pumpGainList=[]

        for i in range(len(probePumpList1)):
            pumpGainList.append(probePumpList2[i]/probePumpList1[i])

        return pumpGainList, pumpWaveList
    else:  #ase gain
        tempList=listSplitter(concatList,concat2)
        probeAseList1=tempList[2]
        probeAseList2=tempList=[5]
        aseWaveList=tempList[8]
        aseGainList=[]

        for i in range(len(probeAseList1)):
            aseGainList.append(probeAseList2[i]/probeAseList1[i])

        return aseGainList, aseWaveList


def noiseFigureProbe(inputSignal,outputSignal) :#not tested 
    tempList=listSplitter(inputSignal,outputSignal)
    WL_sig=tempList[6]
    WL_ase=tempList[8]
    PoutSi=tempList[3]
    PoutEr=tempList[5] 

    hp = 6.62607004e-34 # Planck constant m2kg/s
    c  = 299792458      # Speed of light in vacuum m/s
    
    N_sig = int(0.5*PoutSi.shape[0])
    N_ase = int(0.5*PoutEr.shape[0])

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

    PASE_in  = PoutEr[0:N_ase,0]/DNU_ase      # W/Hz
    PASE_out = PoutEr[0:N_ase,-1]/DNU_ase     # W/Hz
    PASE_in_interp  = interp1d(WL_ase, PASE_in,  kind='linear')   # W/Hz
    PASE_out_interp = interp1d(WL_ase, PASE_out, kind='linear')   # W/Hz
    PASE_in_SigGrid    = PASE_in_interp(WL_sig)      # W/Hz
    PASE_out_SigGrid   = PASE_out_interp(WL_sig)     # W/Hz
    PASE_in_SigGrid    = PASE_in_SigGrid *DNU_sig    # Within Signal bandwidth
    PASE_out_SigGrid   = PASE_out_SigGrid*DNU_sig    # Within Signal bandwidth
    # NF = Pase_added / Gsig*h*v*dv + 1 / Gsig        
    gainhnudeltanu = hp*np.multiply(np.multiply(GainSig,DNU_sig),NU_sig) 
    PASE_added_SigGrid = PASE_out_SigGrid - PASE_in_SigGrid*GainSig
    NF = PASE_added_SigGrid/gainhnudeltanu + 1/GainSig
    
    return NF,gainhnudeltanu