import os
import unittest
import Functions.DateInput
import Functions.PredictHistData
from unittest.mock import patch
class Test_PredictHist(unittest.TestCase):
    DIR = os.path.dirname(os.path.abspath(__file__))
    @patch('builtins.input', return_value='03-11-2023 18:45')
    def test_GetHistInputDate_4(self, mock):
        date = Functions.DateInput.DateInput()
        csv = os.path.join(Test_PredictHist.DIR, 'GetDataForUser.csv')
        result = Functions.PredictHistData.PredictData(csv, date)
        self.assertEqual(result, 4)