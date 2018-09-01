from math import gcd


class Rational:
    def __init__(self, numer: int, denom: int) -> None:
        if denom == 0:
            raise ValueError("denominator must not be zero")

        if denom < 0:
            numer = -numer
            denom = -denom

        gcd_val = gcd(numer, denom)
        self.numer = numer // gcd_val
        self.denom = denom // gcd_val

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Rational): return False
        if self is other: return True
        
        return self.numer == other.numer and self.denom == other.denom

    def __repr__(self) -> str:
        return f"{self.numer}/{self.denom}"

    def __add__(self, other: 'Rational') -> 'Rational':
        return Rational(
            self.numer * other.denom + other.numer * self.denom,
            self.denom * other.denom,
        )

    def __sub__(self, other: 'Rational') -> 'Rational':
        return Rational(
            self.numer * other.denom - other.numer * self.denom,
            self.denom * other.denom,
        )

    def __mul__(self, other: 'Rational') -> 'Rational':
        return Rational(self.numer * other.numer, self.denom * other.denom)

    def __truediv__(self, other: 'Rational') -> 'Rational':
        return Rational(self.numer * other.denom, self.denom * other.numer)

    def __abs__(self) -> 'Rational':
        return Rational(abs(self.numer), abs(self.denom))

    def __pow__(self, power: int) -> 'Rational':
        if power < 0:
            return Rational(self.denom ** power, self.numer ** power)
        return Rational(self.numer ** power, self.denom ** power)

    def __rpow__(self, base: float) -> float:
        return pow(base, self.numer / self.denom)
