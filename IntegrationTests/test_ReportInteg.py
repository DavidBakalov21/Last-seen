import os
import Functions.Input
import Functions.CreateSaveReport
import unittest
from unittest.mock import patch
class RepInteg(unittest.TestCase):
    DIR = os.path.dirname(os.path.abspath(__file__))


    @patch('builtins.input',side_effect = [['min', 'max', 'daily', 'weekly'],['2fba2529-c166-8574-2da2-eac544d82634', '2fba2529-c166-8574-2da2-eac544d826341']])
    def test_ReportInteg_MinMaxDailyWeekly_Ok(self,mock):
        file = os.path.join(RepInteg.DIR, 'ReportTestDataSet')
        metrics=Functions.Input.INput("metrics")
        userList=Functions.Input.INput("users")
        result = Functions.CreateSaveReport.CreateRep(metrics,userList, file)
        self.assertEqual(result, {'2fba2529-c166-8574-2da2-eac544d82634': [{'min time': 3600.0}, {'max time': 25200.0}, {'dailyAverage': 43200.0}, {'WeeklyAverage': 43200.0}], '2fba2529-c166-8574-2da2-eac544d826341': [{'min time': 3600.0}, {'max time': 25200.0}, {'dailyAverage': 43200.0}, {'WeeklyAverage': 43200.0}]})