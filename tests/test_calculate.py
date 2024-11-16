import pytest
from unittest.mock import patch
from calculating import calculate

@pytest.mark.parametrize("fig, func, size, expected_output", [
    ("circle", "area", [5], "area of circle is 78.53981633974483"),
    ("square", "area", [4], "area of square is 16"),
    ("square", "perimeter", [4], "perimeter of square is 16"),
    ("circle", "perimeter", [3], "perimeter of circle is 18.84955592153876"),
])
def test_calculate(fig, func, size, expected_output):
    with patch('builtins.print') as mocked_print:
        calculate.calc(fig, func, size)
    mocked_print.assert_called_with(expected_output)
