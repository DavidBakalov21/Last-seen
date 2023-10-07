import unittest
import Functions.DateInput
import Functions.GetHistoricalData
from unittest.mock import patch
class Test_GetHistInputDate(unittest.TestCase):
    @patch('builtins.input', return_value='04-10-2023 18:45')
    def test_GetHistInputDate_2(self, mock):
        date = Functions.DateInput.DateInput()
        result = Functions.GetHistoricalData.GetData('./GetDataTest', date)
        self.assertEqual(result, {'usersOnline': 2})