import numpy as np
import edfacomponent.splice as spliceobj

def splice_physics(spliceobj):
    Loss_dB = spliceobj.getSpliceLoss()
    Loss    = np.power(10 , -Loss_dB/10 )
    
    InputForward    = spliceobj.getInputForward()
    InputBackward   = spliceobj.getInputBackward()
    OutputForward   = np.multiply(Loss,InputForward)
    OutputBackward  = np.multiply(Loss,InputBackward)
 
    spliceobj.setOutputForward(OutputForward)
    spliceobj.setOutputBackward(OutputBackward)

    
