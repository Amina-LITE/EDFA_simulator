## To test various classes
## Set flag to 1 to test corresponding class
# Control Parameters
import physicslib as ph
import edfacomponent as clist


flag_edf        = 0
flag_connector  = 0
flag_filteropt  = 0
flag_foa        = 0
flag_gff        = 0
flag_iso        = 0
flag_pd         = 0  
flag_splice     = 0
flag_split      = 1
flag_pumpsplit  = 0
flag_switchopt  = 0
flag_voa        = 0
flag_wdm        = 0
flag_source     = 0


if flag_edf : 
    myedf = clist.edf(20,65,'edf1','C-band_cg','componentlayer')
    myedf.setEdfTemp(66)
    myedf.setEdfLength(21)
    print(myedf.getEdfTemp())
    print(myedf.getEdfLength())
    mycomp = myedf
    print(mycomp.getComponentFamily()+ ' '  + mycomp.getComponentName()+ ' ' + mycomp.getComponentType() + ' '+ mycomp.getComponentLayer())
    ph.edf_physics(myedf)
if flag_connector : 
    myconnector = clist.connector(0.1, 'Input', 'LC', 'componentlayer')
    myconnector.setConnectorLoss(0.11)
    print(myconnector.getConnectorLoss())
    mycomp = myconnector
    print(mycomp.getComponentFamily()+ ' '  + mycomp.getComponentName()+ ' ' + mycomp.getComponentType() + ' '+ mycomp.getComponentLayer())

if flag_filteropt : 
    myfiltopt = clist.filteropt(0.45, 'OSC filter', 'TFF' , 'componentlayer')
    myfiltopt.setFilterOptLoss(0.46)
    print(myfiltopt.getFilterOptLoss())
    mycomp = myfiltopt
    print(mycomp.getComponentFamily()+ ' '  + mycomp.getComponentName()+ ' ' + mycomp.getComponentType() + ' '+ mycomp.getComponentLayer()) 
 
if flag_foa : 
    myfoa = clist.foa(5 , 'fixedAtt1' , 'offsetsplice' , 'componentlayer')
    myfoa.setFoaLoss(3)
    myfoa.setInputForward([4,12])
    myfoa.setInputBackward([6,24])
    print(myfoa.getFoaLoss())
    mycomp = myfoa
    print(mycomp.getComponentFamily()+ ' '  + mycomp.getComponentName()+ ' ' + mycomp.getComponentType() + ' '+ mycomp.getComponentLayer()) 
    ph.foa_physics(myfoa)
    print(myfoa.getOutputForward())
    print(myfoa.getOutputBackward())

if flag_gff : 
    mygff = clist.gff([1552, 1554, 1556, 1558] , 0.45 , 'gff1', 'TFF' , 'componentlayer')
    mygff.setGffLoss(0.46)
    test_list = [1552.1, 1554.1, 1556.1, 1558.1]
    mygff.setGffWavelength(test_list)
    print(mygff.getGffLoss())
    print(mygff.getGffWavelength())
    mycomp = mygff
    print(mycomp.getComponentFamily()+ ' '  + mycomp.getComponentName()+ ' ' + mycomp.getComponentType() + ' '+ mycomp.getComponentLayer()) 

if flag_iso : 
    myiso = clist.iso(0.3 , 18 , 'iso1', 'single', 'componentlayer')
    myiso.setIsoLoss(3)
    myiso.setIsoIsolation(20)
    print(myiso.getIsoLoss())
    print(myiso.getIsoIsolation())
    mycomp = myiso
    print(mycomp.getComponentFamily()+ ' '  + mycomp.getComponentName()+ ' ' + mycomp.getComponentType() + ' '+ mycomp.getComponentLayer()) 
    myiso.setInputForward([4,12])
    myiso.setInputBackward([1,100])
    ph.iso_physics(myiso)
    print(myiso.getOutputForward())
    print(myiso.getOutputBackward())



if flag_pd : 
    mypd = clist.pd(0,25,0.98, 'pd1', 'PIN' , 'electroniclayer')
    mypd.setBiasVoltage(0.1)
    mypd.setTemp(26)
    mypd.setResponsivityDis(0.99)
    print(mypd.getBiasVoltage())
    print(mypd.getTemp())
    print(mypd.getRespnsivityDis())
    mycomp = mypd
    print(mycomp.getComponentFamily()+ ' '  + mycomp.getComponentName()+ ' ' + mycomp.getComponentType() + ' '+ mycomp.getComponentLayer()) 

if flag_splice : 
    mysplice = clist.splice(0.03 , 'splice1' , 'smf-smf' , 'componentlayer')
    #mysplice.setSpliceLoss(0.031)
    print(mysplice.getSpliceLoss())
    mycomp = mysplice
    print(mycomp.getComponentFamily()+ ' '  + mycomp.getComponentName()+ ' ' + mycomp.getComponentType() + ' '+ mycomp.getComponentLayer()) 

if flag_split : 
    mysplit = clist.split(3.25, 3.25, 'split1', '50' , 'componentlayer')
    mysplit.setSplitRatio1(3.26)
    mysplit.setSplitRatio2(3.27)
    print(mysplit.getSplitRatio1())
    print(mysplit.getSplitRatio2())
    mycomp = mysplit
    print(mycomp.getComponentFamily()+ ' '  + mycomp.getComponentName()+ ' ' + mycomp.getComponentType() + ' '+ mycomp.getComponentLayer()) 
    mysplit.setInputForward([4,12])
    mysplit.setInputBackward([1,100])
    ph.split_physics(mysplit)
    print(mysplit.getOutputForward())
    print(mysplit.getOutputBackward())
    print(mysplit.getTapOutput())
# if flag_pumpsplit : 
#     mypumpsplit = clist.pumpsplit(3.45, 3.45, 'pumpsplit1', '50' , 'pumplayer')
#     mypumpsplit.setSplitLoss1(3.46)
#     mypumpsplit.setSplitLoss2(3.47)
#     print(mypumpsplit.getSplitLoss1())
#     print(mypumpsplit.getSplitLoss2())
#     mycomp = mypumpsplit
#     print(mycomp.getComponentFamily()+ ' '  + mycomp.getComponentName()+ ' ' + mycomp.getComponentType() + ' '+ mycomp.getComponentLayer()) 

if flag_switchopt : 
    myswitchopt = clist.switchopt(0.4 , 'switch1' , 'MOMEX' , 'componentlayer')
    myswitchopt.setSwitchOptLoss(0.41)
    print(myswitchopt.getSwitchOptLoss())
    mycomp = myswitchopt
    print(mycomp.getComponentFamily()+ ' '  + mycomp.getComponentName()+ ' ' + mycomp.getComponentType() + ' '+ mycomp.getComponentLayer()) 

if flag_voa : 
    myvoa = clist.voa(5 , 'voa1' , 'MATT' , 'componentlayer')
    myvoa.setVoaLoss(5.11)
    print(myvoa.getVoaLoss())
    mycomp = myvoa
    print(mycomp.getComponentFamily()+ ' '  + mycomp.getComponentName()+ ' ' + mycomp.getComponentType() + ' '+ mycomp.getComponentLayer()) 

if flag_wdm : 
    mywdm = clist.wdm(1550 , 0.4 , 50 , 0.9, 50, 'wdm1' , '980/1550' ,'componentlayer')
    mywdm.setcutoff_wl(1550.1)
    mywdm.setlow_wl_loss(0.41)
    mywdm.setlow_wl_isolation(50.1)
    mywdm.sethigh_wl_loss(0.91)
    mywdm.sethigh_wl_isolation(50.2)
    print(mywdm.getcutoff_wl())
    print(mywdm.getlow_wl_loss())
    print(mywdm.getlow_wl_isolation())
    print(mywdm.gethigh_wl_loss())
    print(mywdm.gethigh_wl_isolation())
    mycomp = mywdm
    print(mycomp.getComponentFamily()+ ' '  + mycomp.getComponentName()+ ' ' + mycomp.getComponentType() + ' '+ mycomp.getComponentLayer()) 

if flag_source : 
    mysource = clist.source('singleWL', 974 , 400, 'pump1','pump980', 'pump')
    mysource.setSourceWL(974.1)
    print(mysource.getSourceWL())
    mysource.setSourcePower(403)
    print(mysource.getSourcePower())
    mycomp = mysource
    print(mycomp.getComponentFamily()+ ' '  + mycomp.getComponentName()+ ' ' + mycomp.getComponentType() + ' '+ mycomp.getComponentLayer()) 

    mysource.setOutputForward([1,2,3])
    print(mysource.getOutputForward())


#myvoa.setOutputForward([1,2,3,4])
#print(myvoa.getOutputForward())

#myvoa.setInputForward([1,2,3,4,5])
#print(myvoa.getInputForward())
