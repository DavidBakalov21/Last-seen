import os
import unittest
import DateInput
import TotalTimeOnRange
import inputId
from unittest.mock import patch
class Test_RangeDateId(unittest.TestCase):
    DIR = os.path.dirname(os.path.abspath(__file__))
    @patch('builtins.input',side_effect=['2023-10-10T17:25:41.988544+00:00','2023-10-11T20:21:41.988544+00:00', '2fba2529-c166-8574-2da2-eac544d82634'])
    def test_Range_NormId_32400(self, mock):
        csv = os.path.join(Test_RangeDateId.DIR, 'IntegrationTests/outputRange.csv')
        dateStart= DateInput.DateInput()
        dateEnd = DateInput.DateInput()
        id= inputId.IdInput()
        result = TotalTimeOnRange.TotalTimeRange(csv, id, dateStart, dateEnd)
        self.assertEqual(result, {'totalTime': 32400.0})

    @patch('builtins.input', side_effect=['2023-10-10T17:25:41.988544+00:00', '2023-10-11T20:21:41.988544+00:00',
                                          '2fba2529-c166-8574-adada2da2-eac544d82634'])
    def test_Range_BadId_BadId(self, mock):
        csv = os.path.join(Test_RangeDateId.DIR, 'IntegrationTests/outputRange.csv')
        dateStart = DateInput.DateInput()
        dateEnd = DateInput.DateInput()
        id = inputId.IdInput()
        result = TotalTimeOnRange.TotalTimeRange(csv, id, dateStart, dateEnd)
        self.assertEqual(result, 'ID is wrong')

