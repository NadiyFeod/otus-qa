import pytest
from src.circle import Circle


@pytest.mark.parametrize(
    'r, expected_perimeter, expected_area',
    [
        (12.095775674984045, 76, 459.6394756493937),
        (3.989422804014327, 25.066282746310005, 50),
    ]
)
def test_test_receiving_positive_data(r, expected_perimeter, expected_area):
    obj = Circle(r)
    assert obj.perimeter == expected_perimeter
    assert obj.area == expected_area


@pytest.mark.parametrize(
    'r',
    [
        0,
        -10,
    ]
)
def test_test_receiving_negative_data(r):
    with pytest.raises(ValueError):
        _ = Circle(r)
