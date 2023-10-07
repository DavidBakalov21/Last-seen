import os
import unittest
import Functions.GetHDataForUser

class TestGetData(unittest.TestCase):

    def test__GetDataForUser__04_10_2023_18_45__TrueNone(self):

        result=Functions.GetHDataForUser.GetDataForUser('./GetDataForUser.csv', '04-10-2023 18:45','8c417d9d-b13f-f070-bf07-1fd9c768126f')
        self.assertEqual(result,{"wasUserOnline": True,"nearestOnlineTime": None})

    def test__GetDataForUser__04_10_2023_18_56__FalseNearest(self):
        result = Functions.GetHDataForUser.GetDataForUser('./GetDataForUser.csv', '04-10-2023 18:56','8c417d9d-b13f-f070-bf07-1fd9c768126f')
        self.assertEqual(result, {"wasUserOnline": False, "nearestOnlineTime": '04-10-2023 18:59'})

    def test__GetDataForUser__WrongId__FalseNone(self):
        result = Functions.GetHDataForUser.GetDataForUser('./GetDataForUser.csv', '04-10-2023 18:56','8c417d9d-b1ddd3f-f070-bf07-1fd9c768126f')
        self.assertEqual(result, {"wasUserOnline":False,"nearestOnlineTime": None})