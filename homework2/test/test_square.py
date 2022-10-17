import pytest
from src.square import Square


@pytest.mark.parametrize(
    'a, expected_perimeter, expected_area',
    [
        (10, 40, 100),
        (25,  100, 625),
    ]
)
def test_test_receiving_positive_data(a, expected_perimeter, expected_area):
    obj = Square(a)
    assert obj.perimeter == expected_perimeter
    assert obj.area == expected_area


@pytest.mark.parametrize(
    'a',
    [
        0,
        -5,
    ]
)
def test_test_receiving_negative_data(a):
    with pytest.raises(ValueError):
        _ = Square(a)
