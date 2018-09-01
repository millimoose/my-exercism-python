from enum import Enum, auto
from typing import Dict


class Planet(Enum):
    '''Planets of the solar system'''
    Mercury = auto()
    Earth = auto()
    Venus = auto()
    Mars = auto()
    Jupiter = auto()
    Saturn = auto()
    Uranus = auto()
    Neptune = auto()


class SpaceAge:
    '''Convert a time in seconds to the number of orbital periods ("years") on
    a given planet.
    '''

    # length of year on planet in earth years
    _Ratios: Dict[Planet, float] = {
        Planet.Mercury: 0.2408467,
        Planet.Venus: 0.61519726,
        Planet.Earth: 1.0,
        Planet.Mars: 1.8808158,
        Planet.Jupiter: 11.862615,
        Planet.Saturn: 29.447498,
        Planet.Uranus: 84.016846,
        Planet.Neptune: 164.79132,
    }

    _EarthYearSeconds = 31557600

    def __init__(self, seconds: float) -> None:
        self.seconds = seconds

    def _years_on(self, planet: Planet) -> float:
        '''Convert the seconds value to years on the given planet.'''
        years = self.seconds / (self._EarthYearSeconds * self._Ratios[planet])
        return round(years, 2)

    def on_mercury(self) -> float:
        return self._years_on(Planet.Mercury)

    def on_venus(self) -> float:
        return self._years_on(Planet.Venus)

    def on_earth(self) -> float:
        return self._years_on(Planet.Earth)

    def on_mars(self) -> float:
        return self._years_on(Planet.Mars)

    def on_jupiter(self) -> float:
        return self._years_on(Planet.Jupiter)

    def on_saturn(self) -> float:
        return self._years_on(Planet.Saturn)

    def on_uranus(self) -> float:
        return self._years_on(Planet.Uranus)

    def on_neptune(self) -> float:
        return self._years_on(Planet.Neptune)
