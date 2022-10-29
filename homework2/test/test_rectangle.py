import pytest
from homework2.src.rectangle import Rectangle


@pytest.mark.parametrize(
    'a, b, expected_perimeter, expected_area',
    [
        (10, 15, 50, 150),
        (10, 10, 40, 100),
    ]
)
def test_receiving_positive_data(a, b, expected_perimeter, expected_area):
    obj = Rectangle(a, b)
    assert obj.perimeter == expected_perimeter
    assert obj.area == expected_area


@pytest.mark.parametrize(
    'a, b',
    [
        (0, 0),
        (0, 15),
        (15, 0),
        (-10, 10),
        (24, -26),
        (-5, -7),
    ]
)
def test_receiving_negative_data(a, b):
    with pytest.raises(ValueError):
        _ = Rectangle(a, b)
