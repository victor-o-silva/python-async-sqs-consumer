import pytest

from app.maths import get_semester


@pytest.mark.parametrize(
    "month_value, expected_semester",
    [
        (1, 1),
        (2, 1),
        (3, 1),
        (4, 1),
        (5, 1),
        (6, 1),
    ],
)
def test_get_semester(month_value: int, expected_semester: int):
    result = get_semester(month=month_value)
    assert result == expected_semester
