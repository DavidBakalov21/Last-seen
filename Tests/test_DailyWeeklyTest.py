import os

import Functions.DailyWeekly
import unittest
class TestDailyWeekly(unittest.TestCase):
    DIR = os.path.dirname(os.path.abspath(__file__))
    def test_DailyWeekly_NormId_32400(self):
        csv = os.path.join(TestDailyWeekly.DIR, 'DailyWeekly.csv')
        result = Functions.DailyWeekly.DailyWeekly(csv, '2fba2529-c166-8574-2da2-eac544d82634')
        self.assertEqual(result,{'weeklyAverage':  16200.0, 'dailyAverage': 6480.0})
    def test_DailyWeekly_BadId_BadId(self):
        csv = os.path.join(TestDailyWeekly.DIR, 'DailyWeekly.csv')
        result = Functions.DailyWeekly.DailyWeekly(csv, '2fba2529-c166-8sd574-2da2-easdfgc544d82634')
        self.assertEqual(result, 'bad ID')