import os
import unittest
import Functions.inputId
import Functions.DailyWeekly
from unittest.mock import patch
class Test_DailyWeekly(unittest.TestCase):
    DIR = os.path.dirname(os.path.abspath(__file__))
    @patch('builtins.input', return_value='2fba2529-c166-8574-2da2-eac544d82634')
    def test_DailyWeekly_NormalId_NormData(self, mock):
        csv = os.path.join(Test_DailyWeekly.DIR, 'DailyWeekly.csv')
        id = Functions.inputId.IdInput()
        result = Functions.DailyWeekly.DailyWeekly(csv, id)
        self.assertEqual(result, {'weeklyAverage': 16200.0, 'dailyAverage': 6480.0})

    @patch('builtins.input', return_value='2fba2529-c166-8574-2da2-eacdf5acc44d82634')
    def test_DailyWeekly_NormalId_WrongId(self, mock):
        csv = os.path.join(Test_DailyWeekly.DIR, 'DailyWeekly.csv')
        id = Functions.inputId.IdInput()
        result = Functions.DailyWeekly.DailyWeekly(csv, id)
        self.assertEqual(result, "bad ID")