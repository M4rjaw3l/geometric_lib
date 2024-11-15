import unittest
from unittest.mock import patch
import calculate

class TestCalculate(unittest.TestCase):

    def test_calc_circle_area(self):
        fig = "circle"
        func = "area"
        size = [5]
        expected_output = 'area of circle is 78.53981633974483'

        with patch('builtins.print') as mocked_print:
            calculate.calc(fig, func, size)

        mocked_print.assert_called_with(expected_output)

    def test_calc_square_area(self):
        fig = "square"
        func = "area"
        size = [4]
        expected_output = 'area of square is 16'

        with patch('builtins.print') as mocked_print:
            calculate.calc(fig, func, size)

        mocked_print.assert_called_with(expected_output)

    def test_calc_square_perimeter(self):
        fig = "square"
        func = "perimeter"
        size = [4]
        expected_output = 'perimeter of square is 16'

        with patch('builtins.print') as mocked_print:
            calculate.calc(fig, func, size)

        mocked_print.assert_called_with(expected_output)

    def test_calc_circle_perimeter(self):
        fig = "circle"
        func = "perimeter"
        size = [3]
        expected_output = 'perimeter of circle is 18.84955592153876'

        with patch('builtins.print') as mocked_print:
            calculate.calc(fig, func, size)

        mocked_print.assert_called_with(expected_output)

if __name__ == '__main__':
    unittest.main()
