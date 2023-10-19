
import unittest
import Functions.GetHistoricalData

class TestGetData(unittest.TestCase):

    def test_GetData_04I10I2023_2(self):
        result=Functions.GetHistoricalData.GetData('./GetDataTest', '04-10-2023 18:45')
        self.assertEqual(result,{'usersOnline': 2})

    def test_GetData_04I10I2023_0(self):
        result = Functions.GetHistoricalData.GetData('./GetDataTest', '04-11-2023 18:45')
        self.assertEqual(result, None)