import unittest

from src.function.raiseError import *
from math import pi

class TestCircleArea(unittest.TestCase):
    def test_area(self):
        self.assertEqual(circleArea(1), pi)
        self.assertEqual(circleArea(0), 0)
        self.assertEqual(circleArea(2.34).__round__(2), 17.20)

    def test_negativeRadius(self):
        self.assertRaises(ValueError, circleArea, -2)

    def test_invalidType(self):
        self.assertRaises(TypeError, circleArea, 3-5j)
        self.assertRaises(TypeError, circleArea, "hello")
        self.assertRaises(TypeError, circleArea, None)
        self.assertRaises(TypeError, circleArea, True)
        self.assertRaises(TypeError, circleArea, False)
        self.assertRaises(TypeError, circleArea, (1,2,3))



