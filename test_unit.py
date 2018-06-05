from unittest import TestCase
from conventer import *


class UnitTest(TestCase):
    def test_units(self):
        self.assertEqual(0.1, UnitConverter.conversions["mm"]["cm"])

    def test_info1(self):
        self.assertEqual('Choose the unit you want to convert from? \n The app supports: ' + ", "
                         .join(UnitConverter.conversions.keys()) + " ",
                         'Choose the unit you want to convert from? \n The app supports: mm, cm, m, km, t, kg, g, '
                         'mg, km2, m2, cm2, mm2 ')

    def test_info2(self):
        self.assertEqual("Choose the unit you want to convert to. \n The app supports: " + ", "
                         .join(UnitConverter.conversions.keys()) + " ",
                         'Choose the unit you want to convert to. \n The app supports: mm, cm, m, km, t, kg, g, '
                         'mg, km2, m2, cm2, mm2 ')

    def test_info3(self):
        self.assertEqual("That is not a valid key.", UnitConverter.response)

    def test_result(self):
        self.assertEqual(float, type(UnitConverter.result))

