# component base class with component name, family, type and layer
# 2 Inputs: input forward and input backward
# 2 Output: Output forward and Output backward

class component:
    def __init__(self, cname, ctype, cfamily, component_layer):
        self.component_name   = cname
        self.component_type   = ctype
        self.component_family = cfamily
        self.component_layer  = component_layer
        self.output_f         = []
        self.output_b         = []
        self.input_f          = []
        self.input_b          = []
    
    def getComponentName(self):
        return self.component_name
    
    def setComponentName(self, cname):
        self.component_name = cname

    def getComponentType(self):
        return self.component_type

    def setComponentType(self, ctype):
        self.component_type = ctype
    
    def getComponentFamily(self):
        return self.component_family
    
    def setComponentFamily(self, cfamily):
        self.component_family = cfamily

    def getComponentLayer(self):
        return self.component_layer
    
    def setComponentLayer(self, clayer):
        self.component_layer = clayer

    def getOutputForward(self):
        return self.output_f 

    def setOutputForward(self, ExternalEntry):
        self.output_f = ExternalEntry 

    def getOutputBackward(self):
        return self.output_b 

    def setOutputBackward(self, ExternalEntry):
        self.output_b = ExternalEntry

    def getInputForward(self):
        return self.input_f 

    def setInputForward(self, ExternalEntry):
        self.input_f = ExternalEntry

    def getInputBackward(self):
        return self.input_b 

    def setInputBackward(self, ExternalEntry):
        self.input_b = ExternalEntry
