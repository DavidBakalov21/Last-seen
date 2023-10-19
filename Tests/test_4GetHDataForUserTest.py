import os
import unittest
import Functions.GetHDataForUser

class TestGetData(unittest.TestCase):
    DIR = os.path.dirname(os.path.abspath(__file__))
    def test__GetDataForUser__04_10_2023_18_45__TrueNone(self):
        csv = os.path.join(TestGetData.DIR, 'GetDataForUser.csv')
        result=Functions.GetHDataForUser.GetDataForUser(csv, '04-10-2023 18:45','8c417d9d-b13f-f070-bf07-1fd9c768126f')
        self.assertEqual(result,{"wasUserOnline": True,"nearestOnlineTime": None})

    def test__GetDataForUser__04_10_2023_18_56__FalseNearest(self):
        csv = os.path.join(TestGetData.DIR, 'GetDataForUser.csv')
        result = Functions.GetHDataForUser.GetDataForUser(csv, '04-10-2023 18:56','8c417d9d-b13f-f070-bf07-1fd9c768126f')
        self.assertEqual(result, {"wasUserOnline": False, "nearestOnlineTime": '04-10-2023 18:59'})

    def test__GetDataForUser__WrongId__FalseNone(self):
        csv = os.path.join(TestGetData.DIR, 'GetDataForUser.csv')
        result = Functions.GetHDataForUser.GetDataForUser(csv, '04-10-2023 18:56','8c417d9d-b1ddd3f-f070-bf07-1fd9c768126f')
        self.assertEqual(result, {"wasUserOnline":False,"nearestOnlineTime": None})