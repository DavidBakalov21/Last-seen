import unittest
import warnings

import Functions.PredictHistData



class TestPredictData(unittest.TestCase):

    def test__PredictData__03_11_2023_18_45__4(self):
        warnings.simplefilter(action='ignore', category=Warning)
        result=Functions.PredictHistData.PredictData('./GetDataForUser.csv', '03-11-2023 18:45')
        self.assertEqual(result,4)

    def test__PredictData__04_10_2023_18_45__DataExists(self):
        warnings.simplefilter(action='ignore', category=Warning)
        result = Functions.PredictHistData.PredictData(
            './GetDataForUser.csv', '04-10-2023 18:45')
        self.assertEqual(result,'this date already known')

    def test__PredictData__10_2023_18_10__BadData(self):
        warnings.simplefilter(action='ignore', category=Warning)
        result = Functions.PredictHistData.PredictData(
            './GetDataForUser.csv', '04-10-2023 18:10')
        self.assertEqual(result, 'bad data')


