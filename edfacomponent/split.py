from edfacomponent.component import component

class split(component):
    def __init__(self, split_ratio1, split_ratio2, cname, ctype, clayer, cfamily='split'):
        self.split_ratio1 = split_ratio1
        self.split_ratio2 = split_ratio2
        self.TapOutput = []
        super().__init__(cname, ctype, cfamily , clayer)

    def getSplitRatio1(self):
        return self.split_ratio1
    
    def setSplitRatio1(self, split_ratoi1):
        self.split_ratio1 = split_ratoi1
    
    def getSplitRatio2(self):
        return self.split_ratio2
    
    def setSplitRatio2(self, split_ratio2):
        self.split_ratio2 = split_ratio2

    def getTapOutput(self):
        return self.TapOutput

    def setTapOutput(self, TapOutput):
        self.TapOutput = TapOutput    