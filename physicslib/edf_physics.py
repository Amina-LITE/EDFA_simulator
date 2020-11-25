import edfacomponent.edf as edfobj
from physicslib.EDF3ToolsV2 import LoadCrossSectionData, LoadEDFParams, InitStates, Calculate_Power, Calculate_Derivative, Calculate_SteadyState
import Settings
import numpy as np
def edf_physics(edfobj):
    edfLength = edfobj.getEdfLength()
    edfTemp   = edfobj.getEdfTemp()

    edfobj.setOutputForward(edfobj.getInputForward())
    NS    = 20             # Number of sections considered
     
    CS,gstarhnudeltanu = LoadCrossSectionData(Settings.WL_sig, Settings.WL_pump, Settings.WL_ase,edfTemp)
    Param = LoadEDFParams()
    Ninit = InitStates(NS)
    edfinput = edfobj.getInputForward()
    if edfinput==[] :
       edfinput = np.concatenate((1e-2*np.full((Settings.N_sig,1), 1), 500e-3*np.full((1,1), 1), np.full((Settings.N_ase,1), 0)), axis=0) 
    PinSi = np.full((2*Settings.N_sig,1), 0.0)
    PinPu = np.full((2*Settings.N_pump,1), 0.0)
    PinEr = np.full((2*Settings.N_ase,1), 0.0)
    PinSi[0:Settings.N_sig] = edfinput[0:Settings.N_sig].reshape(Settings.N_sig,1)
    PinPu[0] = edfinput[Settings.N_sig]
    PinEr[0:Settings.N_ase] = edfinput[Settings.N_sig+1:].reshape(Settings.N_ase,1)


    Nss = Calculate_SteadyState(Ninit , PinSi, PinPu, PinEr, Param, CS, NS, edfLength)
    PoutSi, PoutPu, PoutEr,PoutSi_eff, PoutPu_eff, PoutEr_eff= Calculate_Power(Nss , PinSi, PinPu, PinEr ,Param, CS, NS, edfLength)
    dN = Calculate_Derivative(Nss , PinSi, PinPu, PinEr ,Param, CS, NS, edfLength)
    
    edfoutput = np.concatenate((np.squeeze(PoutSi[0:Settings.N_sig,NS] ), (PoutPu[0:1,NS]), np.squeeze(PoutEr[0:Settings.N_ase,NS]))) 
    edfobj.setOutputForward(edfoutput)