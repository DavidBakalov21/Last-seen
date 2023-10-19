import unittest
import Functions.inputId
import Functions.MinMax
from unittest.mock import patch
class Test_TotalTimeIntegration(unittest.TestCase):
    @patch('builtins.input', return_value='2fba2529-c166-8574-2da2-eac544d82634')
    def test_Max_NormalId_25200(self, mock):
        id = Functions.inputId.IdInput()
        result = Functions.MinMax.Max('outputF1.csv', id)
        self.assertEqual(result,  {'max time': 25200.0})

    @patch('builtins.input', return_value='2fba2529-c166-8574-2da2-eac544d82634')
    def test_Min_NormalId_7200(self, mock):
        id = Functions.inputId.IdInput()
        result = Functions.MinMax.Min('outputF1.csv', id)
        self.assertEqual(result, {'min time': 7200.0})

    @patch('builtins.input', return_value='2fba2529-c166-8574-2da2-eac5acc44d82634')
    def test_Min_WrongId_WrongId(self, mock):
        id = Functions.inputId.IdInput()
        result = Functions.MinMax.Min('outputF1.csv', id)
        self.assertEqual(result, "ID is wrong")

    @patch('builtins.input', return_value='2fba2529-c166-8574-2da2-eac5acc44d82634')
    def test_Max_WrongId_WrongId(self, mock):
        id = Functions.inputId.IdInput()
        result = Functions.MinMax.Max('outputF1.csv', id)
        self.assertEqual(result, "ID is wrong")