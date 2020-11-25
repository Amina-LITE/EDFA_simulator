import edfacomponent.source as sourceobj

def source_physics(sourceobj):
    """sourceType  = sourceobj.getSourceType()
    sourceWL    = sourceobj.getSourceWL()
    sourcePower = sourceobj.getSourcePower()

    if (sourceType == 'uniform'):
        sourceobj.setOutputForward(sourcePower)
    elif(sourceType == 'nonuniform'):
        sourceobj.setOutputForward(sourcePower)
    elif(sourceType == 'singleWL'):
        sourceobj.setOutputForward(sourcePower)
    else:
        sourceobj.setOutputForward(0)"""
    sourceobj.setOutputForward(sourceobj.getSourcePower())

    