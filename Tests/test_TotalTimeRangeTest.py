import os

import Functions.TotalTimeOnRange
import unittest
class TotalRangeTest(unittest.TestCase):
    DIR = os.path.dirname(os.path.abspath(__file__))
    def test_TotalRange_NormId_32400(self):
        csv = os.path.join(TotalRangeTest.DIR, 'outputRange.csv')
        result = Functions.TotalTimeOnRange.TotalTimeRange(csv, '2fba2529-c166-8574-2da2-eac544d82634', '2023-10-10T17:25:41.988544+00:00', '2023-10-11T20:21:41.988544+00:00')
        self.assertEqual(result, {'totalTime': 32400.0})


    def test_Max_BadId_BadId(self):
        csv = os.path.join(TotalRangeTest.DIR, 'outputRange.csv')
        result = Functions.TotalTimeOnRange.TotalTimeRange(csv, '2fba2529-c166-8574-2da2-esdfgac544d82634', '2023-10-10T17:25:41.988544+00:00', '2023-10-11T20:21:41.988544+00:00')
        self.assertEqual(result, 'ID is wrong')
