import numpy as np
import edfacomponent.split as splitobj

def split_physics(splitobj):
    Loss_dB1 = splitobj.getSplitRatio1()
    Loss1    = np.power(10 , -Loss_dB1/10 )
    Loss_dB2 = splitobj.getSplitRatio2()
    Loss2    = np.power(10 , -Loss_dB2/10 )

    InputForward    = splitobj.getInputForward()
    InputBackward   = splitobj.getInputBackward()
    OutputForward   = np.multiply(Loss1,InputForward)
    OutputBackward  = np.multiply(Loss1,InputBackward)
    TapOutput       = np.multiply(Loss2,InputForward)
 
    splitobj.setOutputForward(OutputForward)
    splitobj.setOutputBackward(OutputBackward)
    splitobj.setTapOutput(TapOutput)
