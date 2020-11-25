import edfacomponent.iso as isoobj
import numpy as np
def iso_physics(isoobj):
    
    isoobj.setOutputForward(isoobj.getInputForward())

    Loss_dB      = isoobj.getIsoLoss()
    Isolation_dB = isoobj.getIsoIsolation()
    Loss      = np.power(10 , -Loss_dB/10 )
    Isolation = np.power(10 , -Isolation_dB/10 )

    InputForward    = isoobj.getInputForward()
    InputBackward   = isoobj.getInputBackward()
    OutputForward  = np.multiply(Loss,InputForward)
    OutputBackward  = np.multiply(Isolation,InputBackward)

    isoobj.setOutputForward(OutputForward)
    isoobj.setOutputBackward(OutputBackward)