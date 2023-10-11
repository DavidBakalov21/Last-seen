import unittest
import Functions.inputId
import Functions.DailyWeekly
from unittest.mock import patch
class Test_DailyWeekly(unittest.TestCase):
    @patch('builtins.input', return_value='2fba2529-c166-8574-2da2-eac544d82634')
    def test_DailyWeekly_NormalId_NormData(self, mock):
        id = Functions.inputId.IdInput()
        result = Functions.DailyWeekly.DailyWeekly('DailyWeekly.csv', id)
        self.assertEqual(result, {'weeklyAverage': 16200.0, 'dailyAverage': 6480.0})

    @patch('builtins.input', return_value='2fba2529-c166-8574-2da2-eacdf5acc44d82634')
    def test_DailyWeekly_NormalId_WrongId(self, mock):
        id = Functions.inputId.IdInput()
        result = Functions.DailyWeekly.DailyWeekly('DailyWeekly.csv', id)
        self.assertEqual(result, "bad ID")