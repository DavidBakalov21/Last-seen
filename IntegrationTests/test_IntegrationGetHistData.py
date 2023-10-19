import os
import unittest
import Functions.DateInput
import Functions.GetHistoricalData
from unittest.mock import patch
class Test_GetHistInputDate(unittest.TestCase):
    DIR = os.path.dirname(os.path.abspath(__file__))
    @patch('builtins.input', return_value='04-10-2023 18:45')
    def test_GetHistInputDate_2(self, mock):
        csv = os.path.join(Test_GetHistInputDate.DIR, 'GetDataTest')

        date = Functions.DateInput.DateInput()
        result = Functions.GetHistoricalData.GetData(csv, date)
        self.assertEqual(result, {'usersOnline': 2})