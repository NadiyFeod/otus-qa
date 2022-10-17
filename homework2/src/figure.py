class Figure:
    name = "Figure"

    @property
    def area(self):
        raise NotImplementedError

    @property
    def perimeter(self):
        raise NotImplementedError

    def add_area(self, figure):
        return self.area + figure.area
