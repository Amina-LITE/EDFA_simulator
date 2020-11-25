from edfacomponent.component import component

class switchopt(component):
    def __init__(self, switch_opt_loss, cname, ctype, clayer, cfamily='switch_opt'):
        self.switch_opt_loss = switch_opt_loss
        super().__init__(cname, ctype, cfamily , clayer)

    def getSwitchOptLoss(self):
        return self.switch_opt_loss
    
    def setSwitchOptLoss(self, switch_opt_loss):
        self.switch_opt_loss = switch_opt_loss
