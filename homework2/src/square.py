from homework2.src.rectangle import Rectangle


class Square(Rectangle):
    name = "Square"

    def __init__(self, a):
        super().__init__(a, a)
