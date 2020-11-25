from edfacomponent.component import component

class wdm(component):
    def __init__(self, cutoff_wl, low_wl_loss, low_wl_isolation, high_wl_loss, high_wl_isolation, pump, cname, ctype, clayer, cfamily='wdm'):
        self.cutoff_wl = cutoff_wl
        self.low_wl_loss = low_wl_loss
        self.low_wl_isolation = low_wl_isolation
        self.high_wl_loss = high_wl_loss
        self.high_wl_isolation = high_wl_isolation
        self.pump = pump
        super().__init__(cname, ctype, cfamily , clayer)
    
    def getcutoff_wl(self):
        return self.cutoff_wl

    def setcutoff_wl(self, cutoff_wl):
        self.cutoff_wl = cutoff_wl
        
    def getlow_wl_loss(self):
        return self.low_wl_loss

    def setlow_wl_loss(self, low_wl_loss):
        self.low_wl_loss = low_wl_loss
        
    def getlow_wl_isolation(self):
        return self.low_wl_isolation

    def setlow_wl_isolation(self, low_wl_isolation):
        self.low_wl_isolation = low_wl_isolation
        
    def gethigh_wl_loss(self):
        return self.high_wl_loss

    def sethigh_wl_loss(self, high_wl_loss):
        self.high_wl_loss = high_wl_loss
        
    def gethigh_wl_isolation(self):
        return self.high_wl_isolation

    def sethigh_wl_isolation(self, high_wl_isolation):
        self.high_wl_isolation = high_wl_isolation
    
    def getpump(self):
        return self.pump

    def setpump(self, pump):
        self.pump = pump