import os
import unittest
import Functions.GetHistoricalData

class TestGetData(unittest.TestCase):
    DIR = os.path.dirname(os.path.abspath(__file__))
    def test_GetData_04I10I2023_2(self):
        csv = os.path.join(TestGetData.DIR, 'GetDataTest')
        result=Functions.GetHistoricalData.GetData(csv, '04-10-2023 18:45')
        self.assertEqual(result,{'usersOnline': 2})

    def test_GetData_04I10I2023_0(self):
        csv = os.path.join(TestGetData.DIR, 'GetDataTest')
        result = Functions.GetHistoricalData.GetData(csv, '04-11-2023 18:45')
        self.assertEqual(result, None)