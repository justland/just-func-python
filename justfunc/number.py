from dataclasses import dataclass
from math import gcd


@dataclass(frozen=True)
class Ratio:
    numer: int
    denom: int

    @classmethod
    def make(cls, x, y):
        g = gcd(x, y)
        return Ratio(x // g, y // g)

    def __truediv__(self, other):
        if type(other) == Ratio:
            return Ratio.make(self.numer * other.denom, self.denom * other.numer)
        if type(other) == Float:
            return Float((self.numer / self.denom) / other.value)
        if type(other) == Int:
            return self / Ratio.make(other.value, 1)


@dataclass(frozen=True)
class Int:
    value: int

    def __truediv__(self, other):
        if type(other) == Int:
            return Ratio.make(self.value, other.value)
        if type(other) == Ratio:
            return Ratio.make(1, 1) / other
        if type(other) == Float:
            return Float(self.value / other.value)

    def __mul__(self, other):
        if type(other) == Float:
            return Float(self.value * other.value)
        return Int(self.value * other.value)

    def __sub__(self, other):
        return Int(self.value - other.value)

    def __add__(self, other):
        return Int(self.value + other.value)


@dataclass(frozen=True)
class Float:
    value: float

    def __truediv__(self, other):
        if type(other) in [Float, Int]:
            return Float(self.value / other.value)

    def __sub__(self, other):
        return Float(self.value - other.value)

    def __add__(self, other):
        return Float(self.value + other.value)

    def __mul__(self, other):
        return Float(self.value * other.value)
