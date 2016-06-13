"""Contains classes for modeling abstracted models, including their properties
   and relationships. Properties are rarely manipulated directly, but rather
   are declared and defined within a class constructor for a particular model.
"""

class Model(object):
    def __init__(self):
        self._constraints = []
    
    def _getCores(self):
        cores = {}
        for k,v in self.__dict__.iteritems():
            if isinstance(v, Core):
                cores[k] = v
        return cores
        
    def _getAuxes(self):
        auxes = {}
        for k,v in self.__dict__iteritems():
            if isinstance(v, Aux):
                auxes[k] = v
        return auxes
        
    def __setattr__(self, name, value):
        if name in self._getCores():
            prop = getattr(self, name)
            prop.value = value
        else:
            super(Model, self).__setattr__(name, value)
        
class Core(object):
    def __init__(self, name=None, value=None, units=None, err=None):
        self.name = name
        self.value = value
        self.units = units
        self.err = err

class Aux(object):
    def __init__(self, name=None, relationship=None):
        self.name = name
        self.relationship = relationship
        
class Uncert(object):
    def __init__(self, value=0, isAbs=True):
        self.value = value
        self.isAbs = isAbs
