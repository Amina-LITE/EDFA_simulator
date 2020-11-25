from edfacomponent.component import component

class connector(component):
    def __init__(self, connector_loss, cname, ctype, clayer, cfamily='connector'):
        self.connector_loss = connector_loss
        super().__init__(cname, ctype, cfamily , clayer)

    def getConnectorLoss(self):
        return self.connector_loss
    
    def setConnectorLoss(self, connector_loss):
        self.connector_loss = connector_loss
