import pytest
from homework2.src.rectangle import Rectangle
from homework2.src.square import Square
from homework2.src.circle import Circle
from homework2.src.triangle import Triangle


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
        {5, 'a'},
        8,
        'Square(1)',
        None,
    ]
)
def test_negative_result(figure, other_figure):
    with pytest.raises(ValueError):
        _ = figure.add_area(other_figure)
