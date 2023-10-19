import os

import Functions.TotalTime
import unittest
class TestTotalTime(unittest.TestCase):
    DIR = os.path.dirname(os.path.abspath(__file__))
    def test_TimeTotal_NormId_32400(self):
        csv = os.path.join(TestTotalTime.DIR, 'outputF1.csv')
        result = Functions.TotalTime.TotalTime(csv, '2fba2529-c166-8574-2da2-eac544d82634')
        self.assertEqual(result, {'totalTime': 32400.0})
    def test_TimeTotal_BadId_BadId(self):
        csv = os.path.join(TestTotalTime.DIR, 'outputF1.csv')
        result = Functions.TotalTime.TotalTime(csv, '2fba2529-c166-8574-2da2-easdfgc544d82634')
        self.assertEqual(result, 'ID is wrong')

