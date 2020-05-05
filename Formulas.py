import math

G = 6.6743015*10**-11

# simple calculations
def gravity(M:float, r:float) -> float:
    """Gravity Calculation:
    M = mass of planet
    r = radius of planet
    """
    g = G*(M/(r**2))
    return g


def v_orbit(M:float, r:float) -> float:
    """Orbit Velocity:
    M = mass of satellite
    r = distance from planet center to orbit zone
    """
    v = math.sqrt((G*M)/r)
    return v


def period(M:float, r:float) -> float:
    """Orbital period of planet/satellite
    M = mass of planet/satellite
    r = radius from planet
    """
    p2 = (4*math.pi**2*r**3)/(G*M)
    p = math.sqrt(p2)
    return p


