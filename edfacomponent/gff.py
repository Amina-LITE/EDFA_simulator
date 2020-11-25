from edfacomponent.component import component

class gff(component):
    def __init__(self, gff_wavelength, gff_loss, cname, ctype, clayer, cfamily='gff'):
        self.gff_wavelength = gff_wavelength
        self.gff_loss = gff_loss
        super().__init__(cname, ctype, cfamily , clayer)
    
    def getGffWavelength(self):
        return self.gff_wavelength
    
    def getGffLoss(self):
        return self.gff_loss
    
    def setGffWavelength(self, gff_wavelength):
        self.gff_wavelength = gff_wavelength
    
    def setGffLoss(self, gff_loss):
        self.gff_loss = gff_loss

    def physics(self, input):
        return input.append('gff')
    