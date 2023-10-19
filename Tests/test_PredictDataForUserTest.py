import os
import unittest
import warnings

import Functions.PredictForUser

class TestPredictUser(unittest.TestCase):
    DIR = os.path.dirname(os.path.abspath(__file__))
    def test__PredictUser__27_10_2023_18_45__True(self):
        csv = os.path.join(TestPredictUser.DIR, 'UserPredictTest.csv')
        warnings.simplefilter(action='ignore', category=Warning)
        result=Functions.PredictForUser.PredictDataForUser(csv, '27-10-2023 18:45','8c417d9d-b13f-f070-bf07-1fd9c768126f',0.74)
        self.assertEqual(result,{"willBeOnline": True,"onlineChance": 0.75})

    def test__PredictUser__27_10_2023_18_45__False(self):
        csv = os.path.join(TestPredictUser.DIR, 'UserPredictTest.csv')
        warnings.simplefilter(action='ignore', category=Warning)
        result=Functions.PredictForUser.PredictDataForUser(csv, '27-10-2023 18:45','8c417d9d-b13f-f070-bf07-1fd9c768126f',0.9)
        self.assertEqual(result,{"willBeOnline": False,"onlineChance": 0.75})

    def test__PredictUser__05_11_2023_18_45__True(self):
        csv = os.path.join(TestPredictUser.DIR, 'UserPredictTest.csv')
        warnings.simplefilter(action='ignore', category=Warning)
        result=Functions.PredictForUser.PredictDataForUser(csv, '05-11-2023 18:45','8c417d9d-b13f-f070-bf07-1fd9c768126fN',0.99)
        self.assertEqual(result,{"willBeOnline": True,"onlineChance": 1})

    def test__PredictUser__06_10_2023_18_45__AlreadyExists(self):
        csv = os.path.join(TestPredictUser.DIR, 'UserPredictTest.csv')
        warnings.simplefilter(action='ignore', category=Warning)
        result=Functions.PredictForUser.PredictDataForUser(csv, '06-10-2023 18:45','8c417d9d-b13f-f070-bf07-1fd9c768126f',0.99)
        self.assertEqual(result,"this date already known")

    def test__PredictUser__06_10_2023_18_45__BadData(self):
        csv = os.path.join(TestPredictUser.DIR, 'UserPredictTest.csv')
        warnings.simplefilter(action='ignore', category=Warning)
        result=Functions.PredictForUser.PredictDataForUser(csv, '06-10-2023 18:45','8c417d9d-b13f-f070-bf07-1fd9c768126fNOTWORKING',0.99)
        self.assertEqual(result,"not enough data")
