import pytest
from src.triangle import Triangle


@pytest.mark.parametrize(
    'a, b, c, expected_perimeter, expected_area',
    [
        (10, 10, 12, 32, 48),
        (26, 10, 24, 60, 120),
    ]
)
def test_receiving_positive_data(a, b, c, expected_perimeter, expected_area):
    obj = Triangle(a, b, c)
    assert obj.perimeter == expected_perimeter
    assert obj.area == expected_area


@pytest.mark.parametrize(
    'a, b, c',
    [
        (0, 10, 12),
        (1, 2, 3),
        (-26, -10, -24),
    ]
)
def test_receiving_negative_data(a, b, c):
    with pytest.raises(ValueError):
        _ = Triangle(a, b, c)
