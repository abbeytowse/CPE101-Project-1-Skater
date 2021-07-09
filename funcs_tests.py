import unittest
from funcs import *


class TestCases(unittest.TestCase):
    def test_poundsToKG_1(self):
        self.assertAlmostEqual(poundsToKG(0), 0.0)

    def test_poundsToKG_2(self):
        self.assertAlmostEqual(poundsToKG(50), 22.6796)

    def test_poundsToKG_3(self):
        self.assertAlmostEqual(poundsToKG(150.825), 68.4130134)

    def test_getMassObject_1(self):
        self.assertEqual(getMassObject('t'), 0.1)

    def test_getMassObject_2(self):
        self.assertEqual(getMassObject('p'), 1.0)

    def test_getMassObject_3(self):
        self.assertEqual(getMassObject('r'), 3.0)

    def test_getMassObject_4(self):
        self.assertEqual(getMassObject('g'), 5.3)

    def test_getMassObject_5(self):
        self.assertEqual(getMassObject('l'), 9.07)

    def test_getMassObject_6(self):
        self.assertEqual(getMassObject('w'), 0.0)

    def test_getMassObject_7(self):
        self.assertEqual(getMassObject(2), 0.0)

    def test_getVelocityObject_1(self):
        self.assertAlmostEqual(getVelocityObject(0), 0.0)

    def test_getVelocityObject_2(self):
        self.assertAlmostEqual(getVelocityObject(25), 11.06797181)

    def test_getVelocityObject_3(self):
        self.assertAlmostEqual(getVelocityObject(40.356), 14.062162)

    def test_getVelocitySkater_1(self):
        self.assertAlmostEqual(getVelocitySkater(100, 0, 100), 0.0)

    def test_getVelocitySkater_2(self):
        self.assertAlmostEqual(getVelocitySkater(0, 0, 0), 0.0)

    def test_getVelocitySkater_3(self):
        self.assertAlmostEqual(getVelocitySkater(50, 0.1, 15), 0.03)

    def test_getVelocitySkater_4(self):
        self.assertAlmostEqual(getVelocitySkater(68.4017, 9.07, 20), 2.651981)

    def test_getVelocitySkater_5(self):
        self.assertAlmostEqual(getVelocitySkater(22.68, 3.0, 11.0680), 1.464)


if __name__ == '__main__':
    unittest.main()
