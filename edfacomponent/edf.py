from edfacomponent.component import component

class edf(component):
    def __init__(self, length, temp, cname, ctype, clayer, cfamily='edf'):
        self.edf_temp = temp    
        self.edf_length = length
        super().__init__(cname, ctype, cfamily , clayer)
    
    def getEdfLength(self):
        return self.edf_length
    
    def setEdfLength(self, length):
        self.edf_length = length

    def getEdfTemp(self):
        return self.edf_temp
    
    def setEdfTemp(self, temp):
        self.edf_temp = temp
    
    
    