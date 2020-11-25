import json
import time
import edfacomponent
import physicslib
import database as db
import numpy as np
import physicslib as ph
import amp_description as ap
import Settings as settings

from matplotlib import pyplot as plt

def List2Dict_Component(lst): 
    OpticalComponentList = ['Component Family' , 'Component Name', 'Component Type']
    res_dct = {OpticalComponentList[i] : lst[i] for i in range( len(lst))} 
    return res_dct 
OpticalComponentDict =[]
for index in range(ap.OpticalComponent.__len__()):
  OpticalComponentDict.append( List2Dict_Component(ap.OpticalComponent[index]) )
OpticalComponentJson = json.dumps(OpticalComponentDict, indent=4)

def List2Dict_Pump(lst): 
    OpticalPumpList = ['Component Family' , 'Component Name', 'Component Type' , 'port#']
    res_dct = {OpticalPumpList[i] : lst[i] for i in range( len(lst))} 
    return res_dct 
OpticalPumpDict =[]
for index in range(ap.OpticalPump.__len__()):
  OpticalPumpDict.append( List2Dict_Pump(ap.OpticalPump[index]) )
OpticalPumpJson = json.dumps(OpticalPumpDict, indent=4)

def List2Dict_Source(lst): 
    OpticalSourceList = ['Component Family' , 'Component Name', 'Component Type' ]
    res_dct = {OpticalSourceList[i] : lst[i] for i in range( len(lst))} 
    return res_dct 
OpticalSourceDict =[]
for index in range(ap.OpticalSource.__len__()):
  OpticalSourceDict.append( List2Dict_Source(ap.OpticalSource[index]) )
OpticalSourceJson = json.dumps(OpticalSourceDict, indent=4)


def List2Dict_Probe(lst): 
    OpticalProbeList = ['Probe Type' , 'Direction', 'Probe Name' , 'Component/Port1' , 'Component/Port2']
    res_dct = {OpticalProbeList[i] : lst[i] for i in range( len(lst))} 
    return res_dct 
OpticalProbeDict =[]
for index in range(ap.OpticalProbe.__len__()):
  OpticalProbeDict.append( List2Dict_Probe(ap.OpticalProbe[index]) )
OpticalProbeJson = json.dumps(OpticalProbeDict, indent=4)

#print(OpticalComponentDict)   


with open(r'amp.json' , 'w') as f:
  f.write(OpticalProbeJson)
#print(OpticalProbeDict[1]['Probe Type'])

with open(r'amp.json' , 'r') as f:
  OpticalProbeJsonread = f.read() 
  
OpticalProbeJsonreadDict = json.loads(OpticalProbeJsonread)

#print(OpticalProbeJsonreadDict[3]['Probe Type'])
##############################################################