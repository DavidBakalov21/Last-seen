import unittest
import Functions.DateInput
import Functions.GetHDataForUser
import Functions.inputId
from unittest.mock import patch
class Test_GetUserHistInputDateId(unittest.TestCase):
    @patch('builtins.input',side_effect=['04-10-2023 18:45', '8c417d9d-b13f-f070-bf07-1fd9c768126f'])
    def test_GetUserHistInputDateId_TrueNone(self, mock):
        date = Functions.DateInput.DateInput()
        id=Functions.inputId.IdInput()
        result = Functions.GetHDataForUser.GetDataForUser('./GetDataTest', date,id)
        self.assertEqual(result,{"wasUserOnline": True,"nearestOnlineTime": None})