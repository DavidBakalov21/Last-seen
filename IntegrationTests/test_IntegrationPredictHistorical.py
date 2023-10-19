import unittest
import Functions.DateInput
import Functions.PredictHistData
from unittest.mock import patch
class Test_PredictHist(unittest.TestCase):
    @patch('builtins.input', return_value='03-11-2023 18:45')
    def test_GetHistInputDate_4(self, mock):
        date = Functions.DateInput.DateInput()
        result = Functions.PredictHistData.PredictData('./GetDataForUser.csv', date)
        self.assertEqual(result, 4)