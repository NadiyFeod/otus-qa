from math import pi
from src.figure import Figure


class Circle(Figure):
    name = "Circle"

    def __init__(self, r):
        if not (r > 0):
            raise ValueError
        self._r = r

    @property
    def area(self):
        return (self._r * self._r) * pi

    @property
    def perimeter(self):
        return self._r * 2 * pi
