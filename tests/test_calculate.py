import sys
import os
from unittest.mock import patch
import pytest

# Добавляем папку calculating в системный путь
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'calculating')))

import calculate  # Теперь Python может найти calculate.py

@pytest.mark.parametrize("fig, func, size, expected_output", [
    ("circle", "area", [5], "area of circle is 78.53981633974483"),
    ("square", "area", [4], "area of square is 16"),
    ("square", "perimeter", [4], "perimeter of square is 16"),
    ("circle", "perimeter", [3], "perimeter of circle is 18.84955592153876"),
])
def test_calc(fig, func, size, expected_output):
    with patch('builtins.print') as mocked_print:
        calculate.calc(fig, func, size)
    mocked_print.assert_called_with(expected_output)
