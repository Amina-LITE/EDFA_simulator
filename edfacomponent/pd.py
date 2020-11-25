from edfacomponent.component import component

class pd(component):
    def __init__(self, bias_voltage, temp, responsivity_dis, cname, ctype, clayer, cfamily='pd'):
        self.bias_voltage = bias_voltage
        self.temp = temp
        self.responsivity_dis = responsivity_dis
        super().__init__(cname, ctype, cfamily , clayer)

    def getTemp(self):
        return self.temp

    def setTemp(self, temp):
        self.temp = temp

    def getBiasVoltage(self):
        return self.bias_voltage

    def setBiasVoltage(self, bias_voltage):
        self.bias_voltage = bias_voltage

    def getRespnsivityDis(self):
        return self.responsivity_dis

    def setResponsivityDis(self, responsivity_dis):
        self.responsivity_dis = responsivity_dis
    