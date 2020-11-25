import numpy as np
import edfacomponent.connector as connectorobj

def connector_physics(connectorobj):
    Loss_dB = connectorobj.getConnectorLoss()
    Loss    = np.power(10 , -Loss_dB/10 )
    
    InputForward    = connectorobj.getInputForward()
    InputBackward   = connectorobj.getInputBackward()
    OutputForward   = np.multiply(Loss,InputForward)
    OutputBackward  = np.multiply(Loss,InputBackward)
 
    connectorobj.setOutputForward(OutputForward)
    connectorobj.setOutputBackward(OutputBackward)
    