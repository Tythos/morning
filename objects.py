"""Contains classes for modeling abstracted models, including their properties
   and relationships. Properties are rarely manipulated directly, but rather
   are declared and defined within a class constructor for a particular model.
"""

class Model(object):
    def __init__(self):
        self._cores = []
        self._secondaries = []
        self._constraints = []
        
    def getattr(self, name):
        pass
        
    def setattr(self, name, value):
        pass
        
    def _addCore(self, symbol, name=None, value=0., units=None, err=None):
        pass
        
    def _addSecondary(self, symbol, name=None, units=None, relationship=None):
        pass
        
    def _addConstraint(self, constraint):
        pass

class Property(object):
    def __init__(self):
        self.name = None
        self.value = None
        self.units = None
        self.err = None
