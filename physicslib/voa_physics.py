import numpy as np
import edfacomponent.voa as voaobj

def voa_physics(voaobj):
    Loss_dB = voaobj.getVoaLoss()
    Loss    = np.power(10 , -Loss_dB/10 )
    
    InputForward    = voaobj.getInputForward()
    InputBackward   = voaobj.getInputBackward()
    OutputForward   = np.multiply(Loss,InputForward)
    OutputBackward  = np.multiply(Loss,InputBackward)
 
    voaobj.setOutputForward(OutputForward)
    voaobj.setOutputBackward(OutputBackward)
    