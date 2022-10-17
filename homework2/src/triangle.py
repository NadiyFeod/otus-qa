from math import sqrt

from homework2.src.figure import Figure


class Triangle(Figure):
    name = "Triangle"

    def __init__(self, a, b, c):
        if not (a + b > c and a + c > b and b + c > a):
            raise ValueError

        self._a = a
        self._b = b
        self._c = c

    @property
    def area(self):
        p = self.perimeter / 2
        return sqrt(p * (p - self._a) * (p - self._b) * (p - self._c))

    @property
    def perimeter(self):
        return self._a + self._b + self._c
