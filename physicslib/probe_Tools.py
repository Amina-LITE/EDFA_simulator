import numpy as np
import pandas as pd
import Settings as settings
from os.path import join, split, isdir



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