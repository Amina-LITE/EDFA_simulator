import numpy as np
import pandas as pd
import Settings as settings
from glob import glob
from os.path import join, split, isdir



def listSplitter(concatList):
    sigList=concatList[0:settings.N_sig]
    pump=concatList[settings.N_sig]
    aseList=concatList[settings.N_sig+settings.N_pump:]
    return sigList,pump,aseList

def averagePow(signalList):
    temp=0
    for i in signalList:
        temp+=i*i
    average= (1/(2*len(signalList)+1))*temp
    return average

def avgSigPowerProbe(concatList):#double check if this is what Ali wants
    tempList=listSplitter(concatList)
    signalList=tempList[0]
    average= averagePow(signalList)
    return average

def avgASEPowerProbe(concatList):
    tempList=listSplitter(concatList)
    aseList=tempList[2]
    average= averagePow(aseList)
    return average