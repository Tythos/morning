"""Defines based use cases for morning features, to be later transcribed into
   formal test cases.
"""

import morning

class hOrbit(morning.Model):
    def __inif__(self):
        super(Orbit, self).__init__()
        self._addCore('mu',
            name='gravitational parameter'
            value=3.986004418e14,
            units=morning.Units.m**3 / morning.Units.s**2)
        self._addCore('a',
            name='semi-major axis',
            value=4.2167e7,
            units=morning.Units.m,
            err=morning.Uncert(isAbs=True, 0.1) )
        self._addSecondary('T',
            name='period',
            units=morning.Units.s,
            relationship=2*pi*(a**3/mu))
        self._addConstraint(lambda obj: obj.mu>0)
        self._addConstraint(lambda obj: obj.a>0)
           
def main():
    eo = EarthOrbit()
    print(eo)
    eo.a = 4.2167e7 * 0.5
    print(eo)
    eo.a.units = morning.Units.km
    print(eo)
    eo.T = 100 * morning.Units.min
    print(eo)
    eo.a = -1. # should throw an error for violating a constraint

if __name__ == '__main__':
    main()
