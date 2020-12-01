import numpy as np
import edfacomponent.gff as gffobj
import Settings
from physicslib.GFF_tools import Load_GFF_data

def gff_physics(gffobj):
    Loss_dB = gffobj.getGffLoss()
    Loss    = np.power(10 , -Loss_dB/10 )
    gff_Loss = Load_GFF_data(Settings.WL_sig, Settings.WL_pump, Settings.WL_ase,'GFF2') 

    # Gff loss might also need to be converted from dB to linear before multiplying 
    # Need to fix GFF loss shape
    # Both regular loss and GFF loss should be added at this stage 
    
    InputForward    = gffobj.getInputForward()
    InputBackward   = gffobj.getInputBackward()
    OutputForward   = np.multiply(Loss,InputForward)
    OutputBackward  = np.multiply(Loss,InputBackward)
 
    gffobj.setOutputForward(OutputForward)
    gffobj.setOutputBackward(OutputBackward)
  