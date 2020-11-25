import edfacomponent.wdm as wdmobj
import numpy as np
import Settings as st

def wdm_physics(wdmobj):
    
    Loss_1550_dB      = wdmobj.gethigh_wl_loss()
    Loss_1550         = np.power(10 , -Loss_1550_dB/10 )    
    Loss_980_dB       = wdmobj.getlow_wl_loss()
    Loss_980          = np.power(10 , -Loss_980_dB/10 ) 
    Input_pump980     = wdmobj.getpump()
    pump980           = np.multiply(Loss_980,Input_pump980)


    InputForward    = wdmobj.getInputForward()
    InputBackward   = wdmobj.getInputBackward()


    OutputForward   = np.multiply(Loss_1550,InputForward)
    OutputForward[st.N_sig] =  pump980
    OutputBackward  = np.multiply(Loss_1550,InputBackward)
 
    wdmobj.setOutputForward(OutputForward)
    wdmobj.setOutputBackward(OutputBackward)