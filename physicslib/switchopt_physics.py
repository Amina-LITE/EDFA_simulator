import numpy as np
import edfacomponent.switchopt as switchoptobj

def switchopt_physics(switchoptobj):
    Loss_dB = switchoptobj.getSwitchOptLoss()
    Loss    = np.power(10 , -Loss_dB/10 )
    
    InputForward    = switchoptobj.getInputForward()
    InputBackward   = switchoptobj.getInputBackward()
    OutputForward   = np.multiply(Loss,InputForward)
    OutputBackward  = np.multiply(Loss,InputBackward)
 
    switchoptobj.setOutputForward(OutputForward)
    switchoptobj.setOutputBackward(OutputBackward)
