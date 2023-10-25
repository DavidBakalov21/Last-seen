import os
import unittest
import GlobalDataReport

class Test_GetRepFindAv(unittest.TestCase):
    DIR = os.path.dirname(os.path.abspath(__file__))
    def test_GetRepFindAv_data_dict(self):
        file = os.path.join(Test_GetRepFindAv.DIR, 'IntegrationTests/Report')
        data = GlobalDataReport.ReadReportAndWriteData(file)

        result = GlobalDataReport.CalculateAv(data)
        self.assertEqual(result, {'min time': 3600.0, 'max time': 25200.0, 'dailyAverage': 43200.0, 'WeeklyAverage': 43200.0})

