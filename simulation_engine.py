#Main simulation engine where the amp is created and component are connected to the physics library to run different calculations.

import json
import time
import edfacomponent
import physicslib
import database as db
import numpy as np
import physicslib as ph
#set the amp description to work with
import new_amp as ap
import Settings as settings
from physicslib import probe_Tools
from matplotlib import pyplot as plt
import Graphs

# amp array where all the component objects are added to
amp = []

# switch_status turn switches in the amp on and off. True = on and False = off
switch_status = {'SWITCH1' : "off"}

# Creating Source Layer
# sarray is the source layers from the amp description, a is the amp
# CREATES COMPONENTS
# ALWAYS the first component of the amp.
#
# To-do:
# Check if its the first component

def createsourcelayer(sarray,a):
  slen = sarray.__len__()
  for index in range(slen):
    mysource = edfacomponent.source(sarray[index][2],settings.WL, settings.Power,sarray[index][1],sarray[index][2],sarray[index][0],'source')
    ph.source_physics(mysource)
    a.append(mysource)

createsourcelayer(ap.OpticalSource, amp)

# Create Pump Layer
# parray is the pump layer from the amp description
# DOES NOT CREATE ANY COMPONENTS
# Only calculates the total loss of all the components for respective wdms
# Will only go through each pumps
OpticalPumpParsed = {}

def createpumplayer(parray):
  plen = parray.__len__()
  wdm_count = 0
  total_loss = 0
  wdm_lst = []
  pump_dict = {}
  pump_val = 0

  for index in range(plen):
    cFamily = parray[index][0]
    cName   = parray[index][1]
    cType   = parray[index][2]

    if cFamily == "wdm":
      wdm_lst.append(cName)

    #get corresponding pump values according to pump name
    if cFamily == "source":
      pump_val = settings.P_pump[cName]
    
    query_str = 'ComponentFamily == "' + cFamily + '" and ComponentType == "' + cType + '"'
    data = db.excel_db().run_excel_query(query_str)
    total_loss += data["Loss"].item()

  

  val = [total_loss, pump_val]
  wdm_count = wdm_lst.__len__()
  pump_dict = {wdm_lst[i] : val for i in range(wdm_count)}

  #print(pump_dict)

  return pump_dict

#calcualte_pump will go through the Optical Pump layer to add togerther all the pump calculations
def calcualte_pump(parray):
  p_len = parray.__len__()
  for index in range(p_len):
    OpticalPumpParsed.update(createpumplayer(parray[index]))
  
  print(OpticalPumpParsed)
  
calcualte_pump(ap.OpticalPump)

# Main parsing layer that goes through the component layer to 
# create components, 
# calculate their physics, 
# add components to the amp array,
# connects corresponding inputs to outputs
# must make sure source is the first component
def createcomponentlayer(carray, a):
  if a.__len__() == 0:
    print("Array length cannot be 0. check to see if source is added")
    return 0
  
  clen = carray.__len__()
  #to get data from excel table
  df = db.excel_db()  
  
  #adding optical layer to the amp
  for index in range(clen):
    alen = a.__len__()
    # keeping track of previous component 
    PreviousComponent = a[alen-1]    
    OutPutPreviouComponent = PreviousComponent.getOutputForward()
    cFamily = carray[index][0]
    cName   = carray[index][1]
    cType   = carray[index][2]
    cLayer  = 'optical'
    # getting loss values for each component
    query_str = 'ComponentFamily == "' + cFamily + '" and ComponentType == "' + cType + '"'
    data      = df.run_excel_query(query_str)
    print(query_str + ' ComponentName == "' + cName + '"')
    cLoss     = data["Loss"].item()
    
    print("Component loss is " + str(cLoss))

    # Main parsing code
    if cFamily == 'connector':
      component = edfacomponent.connector(cLoss,cName, cType, cLayer, cFamily)
      # Getting output of prev component and setting it as input of current component
      component.setInputForward(OutPutPreviouComponent)
      # calculating physics
      physicslib.connector_physics(component)
    elif cFamily == 'edf':
      #get edf values according to the edf name
      component = edfacomponent.edf(settings.edf_properties[cName]["Len"],settings.edf_properties[cName]["Temp_sim"],cName, cType, cLayer, cFamily)
      component.setInputForward(OutPutPreviouComponent)
      physicslib.edf_physics(component)
    elif cFamily == 'filteropt':
      component = edfacomponent.filteropt(cLoss,cName, cType, cLayer, cFamily)
      component.setInputForward(OutPutPreviouComponent)
      physicslib.filteropt_physics(component)
    elif cFamily == 'foa':
      component = edfacomponent.foa(cLoss,cName, cType, cLayer, cFamily)
      component.setInputForward(OutPutPreviouComponent)
      physicslib.foa_physics(component)
    elif cFamily == 'gff':
      component = edfacomponent.gff(1,cLoss,cName, cType, cLayer, cFamily)  
      component.setInputForward(OutPutPreviouComponent)
      physicslib.gff_physics(component)
    elif cFamily == 'iso':
      component = edfacomponent.iso(cLoss,1,cName, cType, cLayer, cFamily)
      component.setInputForward(OutPutPreviouComponent)
      physicslib.iso_physics(component)
    elif cFamily == 'pd':
      component = edfacomponent.pd(1,1,1,cName, cType, cLayer, cFamily)
      component.setInputForward(OutPutPreviouComponent)
      physicslib.pd_physics(component)
    elif cFamily == 'splice':
      component = edfacomponent.splice(cLoss,cName, cType, cLayer, cFamily)
      component.setInputForward(OutPutPreviouComponent)
      physicslib.splice_physics(component)
    elif cFamily == 'split':
      component = edfacomponent.split(cLoss,1,cName, cType, cLayer, cFamily)
      component.setInputForward(OutPutPreviouComponent)
      physicslib.split_physics(component)
    elif cFamily == 'switchstart':
      # SWITCH
      
      component = edfacomponent.switchopt(cLoss,cName, cType, cLayer, cFamily)
      component.setInputForward(OutPutPreviouComponent)
      physicslib.switchopt_physics(component)
      # if switch is off will add the switch like any other components
      # go through the switch array if switch is on
      # need to add switch twice if switch is on
      if switch_status.get(cName) == "On" or switch_status.get(cName) == "on":
        # adding the current switch to before adding other switch components
        a.append(component)
        # recursively go through this function to create and add switch componets
        createcomponentlayer(ap.SwitchComponent[cName], a)
        # add components to the correct location in the amp
        l = a.__len__()
        # connect the correct output to the input
        PrevComponent = a[l-1]    
        OutPutPrevComponent = PrevComponent.getOutputForward()
        component.setInputForward(OutPutPrevComponent)
        physicslib.switchopt_physics(component)
    elif cFamily == 'tia':
      component = edfacomponent.tia(cName, cType, cLayer, cFamily)
      component.setInputForward(OutPutPreviouComponent)
      physicslib.tia_physics(component)
    elif cFamily == 'voa':
      component = edfacomponent.voa(cLoss,cName, cType, cLayer, cFamily)
      component.setInputForward(OutPutPreviouComponent)
      physicslib.voa_physics(component)
    elif cFamily == 'wdm':
      IL_low = 0
      Pump980Input = 0
      # check if wdm is connected to a pump
      if cName in OpticalPumpParsed.keys():
        #if yes then get corresponding insertion loss and pump values
        IL_low = OpticalPumpParsed[cName][0]
        Pump980Input = OpticalPumpParsed[cName][1]
      else:
        # if not then the values are set to 0
        IL_low = 0
        Pump980Input = 0
      component = edfacomponent.wdm(1,IL_low,1,cLoss,1,Pump980Input, cName, cType, cLayer, cFamily)
      component.setInputForward(OutPutPreviouComponent)
      physicslib.wdm_physics(component) 

    a.append(component)
    print(component.getComponentName())
    print(10*np.log10(component.getOutputForward()[0]/1e-3))

start_time = time.time()
createcomponentlayer(ap.OpticalComponent, amp)

print("--- %s seconds ---" % (time.time() - start_time))
component = amp[-1]
poutamp = component.getOutputForward()

Probe = probe_Tools.Get_Probe_values('Coil1Gain', amp)
Probe2 = probe_Tools.Get_Probe_values('AmplifierGain', amp)        
NFProbe= probe_Tools.Get_Probe_values('AmplifierNF', amp)


#End goal for probes is to be able to call something like 
# Spectrum = probe_Tools.Probe_Spectrum(Probe_name, amp)



# just a simple print function for debugging purposes
def printamp(a):
  for index in range(a.__len__()):
    if a[index].getComponentFamily() == 'splice':
      print( 'Component Family: '+a[index].getComponentFamily() +'\n'+'Component Name: '+ 'splice' +'\n'+'Component Type: '+ a[index].getComponentType()+'\n'+'\n')
    else:
      print('Component Family: '+a[index].getComponentFamily() +'\n'+'Component Name: '+ a[index].getComponentName() +'\n'+'Component Type: '+ a[index].getComponentType()+'\n'+'\n')


Graphs.general_Plot(Probe,"Coil1Gain")#Have to automate this 
Graphs.general_Plot(Probe2,"AmplifierGain")#Have to automate this 
Graphs.general_Plot(NFProbe,"AmplifierNF")#Have to automate this 



Gain = 10*np.log10( poutamp[0:settings.N_sig]/np.squeeze(settings.Signalf.T ))
plt.plot(settings.WL_sig , 10*np.log10( poutamp[0:settings.N_sig]/np.squeeze(settings.Signalf.T )),'-or' )
plt.grid()
plt.xlabel('Wavelength [ nm ]', fontsize = 14)
plt.ylabel('Gain [ dB ]', fontsize = 14)
#plt.xlim(WL_sig_start-5,WL_sig_stop+5)
plt.show()