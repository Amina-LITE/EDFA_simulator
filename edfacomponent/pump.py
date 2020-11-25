from edfacomponent.component import component

class pump(component):
    def __init__(self, pump_wavelength, pump_power, cname, ctype, clayer, cfamily='pump'):
        self.pump_wavelength = pump_wavelength
        self.pump_power = pump_power
        super().__init__(cname, ctype, cfamily , clayer)
    
    def getPumpWavelength(self):
        return self.pump_wavelength
    
    def getPumpPower(self):
        return self.pump_power
    
    def setPumpWavelength(self, pump_wavelength):
        self.pump_wavelength = pump_wavelength
    
    def setPumpPower(self, pump_power):
        self.pump_power = pump_power
    
    