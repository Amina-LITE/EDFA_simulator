import numpy as np
import edfacomponent.pumpsplit as pumpsplitobj

def pumpsplit_physics(pumpsplitobj):
    Loss_dB1 = splitobj.getSplitRatio1()
    Loss1    = np.power(10 , -Loss_dB1/10 )
    Loss_dB2 = splitobj.getSplitRatio2()
    Loss2    = np.power(10 , -Loss_dB2/10 )
    
    InputForward    = pumpsplitobj.getInputForward()
    InputBackward   = pumpsplitobj.getInputBackward()
    OutputForward   = np.multiply(Loss1,InputForward)
    OutputBackward  = np.multiply(Loss1,InputBackward)
 
    pumpsplitobj.setOutputForward(OutputForward)
    pumpsplitobj.setOutputBackward(OutputBackward)
    