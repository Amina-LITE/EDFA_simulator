import numpy as np
import edfacomponent.gff as gffobj

def gff_physics(gffobj):
    Loss_dB = gffobj.getGffLoss()
    Loss    = np.power(10 , -Loss_dB/10 )
    
    InputForward    = gffobj.getInputForward()
    InputBackward   = gffobj.getInputBackward()
    OutputForward   = np.multiply(Loss,InputForward)
    OutputBackward  = np.multiply(Loss,InputBackward)
 
    gffobj.setOutputForward(OutputForward)
    gffobj.setOutputBackward(OutputBackward)
  