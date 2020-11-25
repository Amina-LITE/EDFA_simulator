from edfacomponent.component import  component
class source(component):      
    def __init__(self, stype, sWL, spower, cname, ctype, clayer, cfamily='source'):
        self.source_type             = stype
        self.source_wl               = sWL
        self.source_power            = spower
        super().__init__(cname, ctype, cfamily , clayer)
    
    def getSourceType(self):
        return self.source_type
    
    def setSourceType(self, stype):
        self.source_type = stype

    def getSourceWL(self):
        return self.source_wl
    
    def setSourceWL(self, sWL):
        self.source_wl = sWL

    def getSourcePower(self):
        return self.source_power
    
    def setSourcePower(self, spower):
        self.source_power = spower

    
