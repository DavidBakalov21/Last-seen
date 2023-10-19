import unittest
import Functions.DateInput
import Functions.PredictForUser
import Functions.inputId
from unittest.mock import patch
class Test_PredictUserHistInputDateId(unittest.TestCase):
    @patch('builtins.input',side_effect=['27-10-2023 18:45', '8c417d9d-b13f-f070-bf07-1fd9c768126f'])
    def test_PredictUserHistInputDateId_True(self, mock):
        date = Functions.DateInput.DateInput()
        id=Functions.inputId.IdInput()
        result = Functions.PredictForUser.PredictDataForUser('./UserPredictTest.csv', date,id,0.74)
        self.assertEqual(result,{"willBeOnline": True,"onlineChance": 0.75})