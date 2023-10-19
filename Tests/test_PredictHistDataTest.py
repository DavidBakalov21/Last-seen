import os
import unittest
import warnings

import Functions.PredictHistData



class TestPredictData(unittest.TestCase):
    DIR = os.path.dirname(os.path.abspath(__file__))
    def test__PredictData__03_11_2023_18_45__4(self):
        csv = os.path.join(TestPredictData.DIR, 'GetDataForUser.csv')
        warnings.simplefilter(action='ignore', category=Warning)
        result=Functions.PredictHistData.PredictData(csv, '03-11-2023 18:45')
        self.assertEqual(result,4)

    def test__PredictData__04_10_2023_18_45__DataExists(self):
        csv = os.path.join(TestPredictData.DIR, 'GetDataForUser.csv')
        warnings.simplefilter(action='ignore', category=Warning)
        result = Functions.PredictHistData.PredictData(
            csv, '04-10-2023 18:45')
        self.assertEqual(result,'this date already known')

    def test__PredictData__10_2023_18_10__BadData(self):
        csv = os.path.join(TestPredictData.DIR, 'GetDataForUser.csv')
        warnings.simplefilter(action='ignore', category=Warning)
        result = Functions.PredictHistData.PredictData(
            csv, '04-10-2023 18:10')
        self.assertEqual(result, 'bad data')


