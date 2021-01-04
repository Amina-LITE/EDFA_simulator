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