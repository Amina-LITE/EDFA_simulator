import numpy as np
import edfacomponent.foa as foaobj

def foa_physics(foaobj):

    Loss_dB = foaobj.getFoaLoss()
    Loss    = np.power(10 , -Loss_dB/10 )
    
    InputForward    = foaobj.getInputForward()
    InputBackward   = foaobj.getInputBackward()
    OutputForward   = np.multiply(Loss,InputForward)
    OutputBackward  = np.multiply(Loss,InputBackward)
 
    foaobj.setOutputForward(OutputForward)
    foaobj.setOutputBackward(OutputBackward)
    