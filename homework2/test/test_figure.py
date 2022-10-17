import pytest
from src.rectangle import Rectangle
from src.square import Square
from src.circle import Circle
from src.triangle import Triangle


@pytest.mark.parametrize(
    'figure',
    [
        (Rectangle(10, 20)),
        (Circle(3)),
        (Square(7)),
        (Triangle(11, 12, 13)),
    ]
)
@pytest.mark.parametrize(
    'other_figure',
    [
        (Rectangle(5, 2)),
        (Circle(7)),
        (Square(1)),
        (Triangle(15, 16, 17)),
    ]
)
def test_positive_result(figure, other_figure):
    assert figure.add_area(other_figure) == figure.area + other_figure.area
