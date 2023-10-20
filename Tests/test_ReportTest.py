import os

import Functions.CreateSaveReport
import unittest
class Report(unittest.TestCase):
    DIR = os.path.dirname(os.path.abspath(__file__))

    def test_Report_MinMaxDailyWeekly_Ok(self):
        file = os.path.join(Report.DIR, 'ReportTestDataSet')
        result = Functions.CreateSaveReport.CreateRep(['min', 'max', 'daily', 'weekly'], ['2fba2529-c166-8574-2da2-eac544d82634','2fba2529-c166-8574-2da2-eac544d826341'],file)
        self.assertEqual(result, {'2fba2529-c166-8574-2da2-eac544d82634': [{'min time': 3600.0}, {'max time': 25200.0}, {'dailyAverage': 43200.0}, {'WeeklyAverage': 43200.0}], '2fba2529-c166-8574-2da2-eac544d826341': [{'min time': 3600.0}, {'max time': 25200.0}, {'dailyAverage': 43200.0}, {'WeeklyAverage': 43200.0}]})