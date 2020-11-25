from edfacomponent.component import component

class foa(component):
    def __init__(self, foa_loss, cname, ctype, clayer, cfamily='foa'):
        self.foa_loss = foa_loss
        super().__init__(cname, ctype, cfamily , clayer)

    def getFoaLoss(self):
        return self.foa_loss
    
    def setFoaLoss(self, foa_loss):
        self.foa_loss = foa_loss
