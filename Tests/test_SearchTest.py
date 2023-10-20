import os

import Functions.CreateSaveReport
import unittest
class Search(unittest.TestCase):
    DIR = os.path.dirname(os.path.abspath(__file__))

    def test_Report_Rep1_Ok(self):
        file = os.path.join(Search.DIR, 'Report')
        result = Functions.CreateSaveReport.SearchReport('Rep1', file)
        self.assertEqual(result, ['Report Name: Rep1',
 '2fba2529-c166-8574-2da2-eac544d82634:',
 "[{'min time': 3600.0}, {'max time': 25200.0}, {'dailyAverage': 43200.0}, "
 "{'WeeklyAverage': 43200.0}]",
 '2fba2529-c166-8574-2da2-eac544d826341:',
 "[{'min time': 3600.0}, {'max time': 25200.0}, {'dailyAverage': 43200.0}, "
 "{'WeeklyAverage': 43200.0}]"])