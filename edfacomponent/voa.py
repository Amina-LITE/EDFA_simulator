from edfacomponent.component import component

class voa(component):
    def __init__(self, voa_loss, cname, ctype, clayer, cfamily='voa'):
        self.voa_loss = voa_loss
        super().__init__(cname, ctype, cfamily , clayer)

    def getVoaLoss(self):
        return self.voa_loss
    
    def setVoaLoss(self, voa_loss):
        self.voa_loss = voa_loss
