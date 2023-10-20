import os
import Functions.Input
import Functions.CreateSaveReport
import unittest
from unittest.mock import patch
class Test_RepInteg(unittest.TestCase):
    DIR = os.path.dirname(os.path.abspath(__file__))
    @patch('builtins.input', return_value='Rep1')
    def test_PredictUserHistInputDateId_True(self, mock):
        file = os.path.join(Test_RepInteg.DIR, 'Report')
        name = Functions.Input.INput("name")
        result = Functions.CreateSaveReport.SearchReport(name, file)
        self.assertEqual(result,['Report Name: Rep1',
 '2fba2529-c166-8574-2da2-eac544d82634:',
 "[{'min time': 3600.0}, {'max time': 25200.0}, {'dailyAverage': 43200.0}, "
 "{'WeeklyAverage': 43200.0}]",
 '2fba2529-c166-8574-2da2-eac544d826341:',
 "[{'min time': 3600.0}, {'max time': 25200.0}, {'dailyAverage': 43200.0}, "
 "{'WeeklyAverage': 43200.0}]"])