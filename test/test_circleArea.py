import unittest
from src.function.area import *
from math import pi

class TestCircleArea(unittest.Testcase):
    def test_area(self):
        self.assertEqual(circleArea(1), pi)