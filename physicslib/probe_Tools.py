import numpy as np
import pandas as pd
from glob import glob
from os.path import join, split, isdir
from Settings import * 


def listSplitter(concatList):
    sigList=concatList[0:100]
    pump=concatList[100]
    aseList=concatList[101:]
    return sigList,pump,aseList