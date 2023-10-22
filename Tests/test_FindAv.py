import Functions.GlobalDataReport
import unittest
class FindAv(unittest.TestCase):
    def test_FindAv_Data_Dict(self):
        result = Functions.GlobalDataReport.CalculateAv([{'min time': 3600.0}, {'max time': 25200.0}, {'dailyAverage': 43200.0}, {'WeeklyAverage': 43200.0}, {'min time': 3600.0}, {'max time': 25200.0}, {'dailyAverage': 43200.0}, {'WeeklyAverage': 43200.0}, {'min time': 3600.0}, {'max time': 25200.0}, {'dailyAverage': 43200.0}, {'WeeklyAverage': 43200.0}, {'min time': 3600.0}, {'max time': 25200.0}, {'dailyAverage': 43200.0}, {'WeeklyAverage': 43200.0}])
        self.assertEqual(result,{'min time': 3600.0, 'max time': 25200.0, 'dailyAverage': 43200.0, 'WeeklyAverage': 43200.0})