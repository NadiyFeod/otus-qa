from src.figure import Figure


class Rectangle(Figure):
    name = "Rectangle"

    def __init__(self, a, b):
        if not (a > 0 and b > 0):
            raise ValueError

        self._a = a
        self._b = b

    @property
    def area(self):
        return self._a * self._b

    @property
    def perimeter(self):
        return 2 * (self._a + self._b)
