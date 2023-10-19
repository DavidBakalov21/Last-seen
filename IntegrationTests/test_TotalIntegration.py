import os
import unittest
import Functions.inputId
import Functions.TotalTime
from unittest.mock import patch
class Test_TotalTimeIntegration(unittest.TestCase):
    DIR = os.path.dirname(os.path.abspath(__file__))
    @patch('builtins.input', return_value='2fba2529-c166-8574-2da2-eac544d82634')
    def test_TotalTime_NormalId_32400(self, mock):
        csv = os.path.join(Test_TotalTimeIntegration.DIR, 'outputF1.csv')
        id = Functions.inputId.IdInput()
        result = Functions.TotalTime.TotalTime(csv, id)
        self.assertEqual(result, {'totalTime': 32400.0})

    @patch('builtins.input', return_value='2fba2529-c166-8574-2da2-eac5acc44d82634')

    def test_TotalTime_NormalId_WrongId(self, mock):
        csv = os.path.join(Test_TotalTimeIntegration.DIR, 'outputF1.csv')
        id = Functions.inputId.IdInput()
        result = Functions.TotalTime.TotalTime(csv, id)
        self.assertEqual(result, "ID is wrong")