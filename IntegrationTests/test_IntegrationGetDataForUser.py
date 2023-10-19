import os
import unittest
import Functions.DateInput
import Functions.GetHDataForUser
import Functions.inputId
from unittest.mock import patch
class Test_GetUserHistInputDateId(unittest.TestCase):
    DIR = os.path.dirname(os.path.abspath(__file__))
    @patch('builtins.input',side_effect=['04-10-2023 18:45', '8c417d9d-b13f-f070-bf07-1fd9c768126f'])
    def test_GetUserHistInputDateId_TrueNone(self, mock):
        csv = os.path.join(Test_GetUserHistInputDateId.DIR, 'GetDataTest')
        date = Functions.DateInput.DateInput()
        id=Functions.inputId.IdInput()
        result = Functions.GetHDataForUser.GetDataForUser(csv, date,id)
        self.assertEqual(result,{"wasUserOnline": True,"nearestOnlineTime": None})