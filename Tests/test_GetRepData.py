import os

import Functions.GlobalDataReport
import unittest
class GetDataFromRep(unittest.TestCase):
    DIR = os.path.dirname(os.path.abspath(__file__))

    def test_ReadReportAndWriteData_Rep1_Dict(self):
        file = os.path.join(GetDataFromRep.DIR, 'Report')
        result = Functions.GlobalDataReport.ReadReportAndWriteData(file)
        self.assertEqual(result,[{'min time': 3600.0}, {'max time': 25200.0}, {'dailyAverage': 43200.0}, {'WeeklyAverage': 43200.0}, {'min time': 3600.0}, {'max time': 25200.0}, {'dailyAverage': 43200.0}, {'WeeklyAverage': 43200.0}, {'min time': 3600.0}, {'max time': 25200.0}, {'dailyAverage': 43200.0}, {'WeeklyAverage': 43200.0}, {'min time': 3600.0}, {'max time': 25200.0}, {'dailyAverage': 43200.0}, {'WeeklyAverage': 43200.0}])
