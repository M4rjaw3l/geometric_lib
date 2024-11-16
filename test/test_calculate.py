import sys
import os


sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import unittest
from calculate import calc
import circle
import square
from io import StringIO
import sys

class TestCalculate(unittest.TestCase):
    def setUp(self):
        self.saved_stdout = sys.stdout
        sys.stdout = StringIO()

    def tearDown(self):
        sys.stdout = self.saved_stdout

    def test_circle_area(self):
        size = [5]
        expected_output = "area of circle is 78.53981633974483\n"
        calc('circle', 'area', size)
        output = sys.stdout.getvalue()
        self.assertEqual(output, expected_output)

    def test_circle_perimeter(self):
        size = [5]
        expected_output = "perimeter of circle is 31.41592653589793\n"
        calc('circle', 'perimeter', size)
        output = sys.stdout.getvalue()
        self.assertEqual(output, expected_output)

    def test_square_area(self):
        size = [4]
        expected_output = "area of square is 16\n"
        calc('square', 'area', size)
        output = sys.stdout.getvalue()
        self.assertEqual(output, expected_output)

    def test_square_perimeter(self):
        size = [4]
        expected_output = "perimeter of square is 16\n"
        calc('square', 'perimeter', size)
        output = sys.stdout.getvalue()
        self.assertEqual(output, expected_output)

if __name__ == '__main__':
    unittest.main()



