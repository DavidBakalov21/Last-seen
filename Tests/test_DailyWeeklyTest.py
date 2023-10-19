
import Functions.DailyWeekly 
import unittest
class TestDailyWeekly(unittest.TestCase):

    def test_DailyWeekly_NormId_32400(self):
        result = Functions.DailyWeekly.DailyWeekly('DailyWeekly.csv', '2fba2529-c166-8574-2da2-eac544d82634')
        self.assertEqual(result,{'weeklyAverage':  16200.0, 'dailyAverage': 6480.0})
    def test_DailyWeekly_BadId_BadId(self):
        result = Functions.DailyWeekly.DailyWeekly('DailyWeekly.csv', '2fba2529-c166-8sd574-2da2-easdfgc544d82634')
        self.assertEqual(result, 'bad ID')