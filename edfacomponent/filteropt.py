from edfacomponent.component import component

class filteropt(component):
    def __init__(self, filter_opt_loss, cname, ctype, clayer, cfamily='filter_opt'):
        self.filter_opt_loss = filter_opt_loss
        super().__init__(cname, ctype, cfamily , clayer)

    def getFilterOptLoss(self):
        return self.filter_opt_loss
    
    def setFilterOptLoss(self, filter_opt_loss):
        self.filter_opt_loss = filter_opt_loss
