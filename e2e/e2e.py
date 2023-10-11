import unittest
from datetime import timedelta, datetime, timezone

from Functions import FormatData
from Functions import ConvertToReadable
from Functions import GetHistoricalData
from Functions import GetHDataForUser
from Functions import PredictHistData
from Functions import PredictForUser
from Functions import DeleteUser
from Functions import TotalTime
from Functions import Translate
import Functions.DailyWeekly

class TestLastSeen(unittest.TestCase):

    def test_e2e(self):
        result = ConvertToReadable.ConvertToReadable({"user": True}, "1")
        self.assertEqual(result, "User " + "user" + " is online")
        result2 = ConvertToReadable.ConvertToReadable({"user": True}, "2")
        self.assertEqual(result2, "Користувач " + "user" + " онлайн")
        result = ConvertToReadable.ConvertToReadable(
            {"user": timedelta(hours=0, minutes=16, seconds=59, microseconds=384718)}, "1")
        self.assertEqual(result,
                         "User " + "user" + " was last seen at " + "0:16:59.384718" + " (couple of minutes ago)")
        result2 = ConvertToReadable.ConvertToReadable(
            {"user": timedelta(hours=0, minutes=16, seconds=59, microseconds=384718)}, "2")
        self.assertEqual(result2,
                         "Користувач " + "user" + " в останнє був присутній " + "0:16:59.384718" + " (декілька хвилин тому)")
        result = Functions.DailyWeekly.DailyWeekly('DailyWeekly.csv', '2fba2529-c166-8574-2da2-eac544d82634')
        self.assertEqual(result, {'weeklyAverage': 16200.0, 'dailyAverage': 6480.0})
        result = Functions.DailyWeekly.DailyWeekly('DailyWeekly.csv', '2fba2529-c166-8sd574-2da2-easdfgc544d82634')
        self.assertEqual(result, 'bad ID')
        result = Functions.DeleteUser.DeleteData('DelTest.csv', '2fba2529-c166-8sashjkd574-2da2-easdfgc544d82634')
        self.assertEqual(result, "user wasn't present or id was incorect")
        result = Functions.FormatData.FormatData(
            {'userId': '2fba2529-c166-8574-2da2-eac544d82634', 'nickname': 'Doug93', 'firstName': 'Doug',
             'lastName': 'Rogahn', 'registrationDate': '2023-06-04T03:53:45.4490942+00:00',
             'lastSeenDate': '2023-09-24T15:22:42.9695297+00:00', 'isOnline': False})
        self.assertEqual(result, datetime.now().astimezone(timezone.utc) - datetime.fromisoformat(
            "2023-09-24T15:22:42.9695297+00:00"))
        result = Functions.GetHDataForUser.GetDataForUser('./GetDataForUser.csv', '04-10-2023 18:45',
                                                          '8c417d9d-b13f-f070-bf07-1fd9c768126f')
        self.assertEqual(result, {"wasUserOnline": True, "nearestOnlineTime": None})
        result = Functions.GetHDataForUser.GetDataForUser('./GetDataForUser.csv', '04-10-2023 18:56',
                                                          '8c417d9d-b13f-f070-bf07-1fd9c768126f')
        self.assertEqual(result, {"wasUserOnline": False, "nearestOnlineTime": '04-10-2023 18:59'})
        result = Functions.GetHistoricalData.GetData('./GetDataTest', '04-11-2023 18:45')
        self.assertEqual(result, None)
        result = Functions.PredictForUser.PredictDataForUser('./UserPredictTest.csv', '27-10-2023 18:45',
                                                             '8c417d9d-b13f-f070-bf07-1fd9c768126f', 0.74)
        self.assertEqual(result, {"willBeOnline": True, "onlineChance": 0.75})
        result = Functions.PredictHistData.PredictData('./GetDataForUser.csv', '03-11-2023 18:45')
        self.assertEqual(result, 4)
        result = Functions.Translate.Translate("1")
        self.assertEqual(result, ["User ", " was last seen at ", " (just now)", " (less than a minute ago)",
                                  " (couple of minutes ago)",
                                  " (hour ago)", " (today)", " (yesterday)", " (this week)", " (Long ago)",
                                  " is online"])
        result = Functions.TotalTime.TotalTime('outputF1.csv', '2fba2529-c166-8574-2da2-eac544d82634')
        self.assertEqual(result, {'totalTime': 32400.0})
        result = Functions.TotalTime.TotalTime('outputF1.csv', '2fba2529-c166-8574-2da2-easdfgc544d82634')
        self.assertEqual(result, 'ID is wrong')
