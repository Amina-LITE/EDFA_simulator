import numpy as np
import edfacomponent.gff as gffobj
import Settings
from physicslib.GFF_tools import Load_GFF_data

def gff_physics(gffobj):
    Loss_dB = gffobj.getGffLoss()
    Loss    = np.power(10 , -Loss_dB/10 )
    gff_Loss_db = Load_GFF_data(Settings.WL_sig, Settings.WL_pump, Settings.WL_ase,gffobj.component_name) 
    gff_Loss    = np.power(10 , np.negative(gff_Loss_db)/10 )
    # Gff loss might also need to be converted from dB to linear before multiplying 
    # Need to fix GFF loss shape
    # Both regular loss and GFF loss should be added at this stage 
    #Check if multiply is the correct operation or maybe its addition for the loss
    InputForward    = gffobj.getInputForward()
    InputBackward   = gffobj.getInputBackward()

    OutputForward_interim   = np.multiply(Loss,InputForward)
    OutputBackward  = np.multiply(Loss,InputBackward)

    OutputForward = np.multiply(gff_Loss,OutputForward_interim)
    #OutputBackward  = np.multiply(gff_Loss,OutputBackward_interim)

    gffobj.setOutputForward(OutputForward)
    gffobj.setOutputBackward(OutputBackward)
  