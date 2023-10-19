import os

import Functions.MinMax
import unittest
class MinMaxTest(unittest.TestCase):
    DIR = os.path.dirname(os.path.abspath(__file__))

    def test_Max_NormId_25200(self):
        csv = os.path.join(MinMaxTest.DIR, 'outputF1.csv')
        result = Functions.MinMax.Max(csv, '2fba2529-c166-8574-2da2-eac544d82634')
        self.assertEqual(result, {'max time': 25200.0})

    def test_Min_NormId_7200(self):
        csv = os.path.join(MinMaxTest.DIR, 'outputF1.csv')
        result = Functions.MinMax.Min(csv, '2fba2529-c166-8574-2da2-eac544d82634')
        self.assertEqual(result, {'min time': 7200.0})
    def test_Min_BadId_BadId(self):
        csv = os.path.join(MinMaxTest.DIR, 'outputF1.csv')
        result = Functions.MinMax.Min(csv, '2fba2529-c166-8574-2da2-easdfgc544d82634')
        self.assertEqual(result, 'ID is wrong')
    def test_Max_BadId_BadId(self):
        csv = os.path.join(MinMaxTest.DIR, 'outputF1.csv')
        result = Functions.MinMax.Max(csv, '2fba2529-c166-8574-2da2-easdfgc544d82634')
        self.assertEqual(result, 'ID is wrong')
