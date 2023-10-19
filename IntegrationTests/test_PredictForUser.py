import os
import unittest
import Functions.DateInput
import Functions.PredictForUser
import Functions.inputId
from unittest.mock import patch
class Test_PredictUserHistInputDateId(unittest.TestCase):
    DIR = os.path.dirname(os.path.abspath(__file__))
    @patch('builtins.input',side_effect=['27-10-2023 18:45', '8c417d9d-b13f-f070-bf07-1fd9c768126f'])
    def test_PredictUserHistInputDateId_True(self, mock):
        csv = os.path.join(Test_PredictUserHistInputDateId.DIR, 'UserPredictTest.csv')
        date = Functions.DateInput.DateInput()
        id=Functions.inputId.IdInput()
        result = Functions.PredictForUser.PredictDataForUser(csv, date,id,0.74)
        self.assertEqual(result,{"willBeOnline": True,"onlineChance": 0.75})