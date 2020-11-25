from edfacomponent.component import component

class iso(component):
    def __init__(self, iso_loss, iso_isolation, cname, ctype, clayer, cfamily='iso'):
        self.iso_loss = iso_loss
        self.iso_isolation = iso_isolation
        super().__init__(cname, ctype, cfamily , clayer)
    
    def getIsoIsolation(self):
        return self.iso_isolation
    
    def getIsoLoss(self):
        return self.iso_loss
    
    def setIsoIsolation(self, iso_isolation):
        self.iso_isolation = iso_isolation
    
    def setIsoLoss(self, iso_loss):
        self.iso_loss = iso_loss

    def physics(self, input):
        return input.append('iso')
