class probe:
    def __init__(self, connection_a, connection_b):
        self.connection_a = connection_a
        self.connection_b = connection_b
    
    def getConnectionA(self):
        return self.connection_a
    
    def getConnectionB(self):
        return self.connection_b
    
    def setConnectionA(self, connection_a):
        self.connection_a = connection_a
    
    def setConnectionB(self, connection_b):
        self.connection_b = connection_b
    