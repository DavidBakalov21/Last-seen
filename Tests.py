import unittest
from datetime import timedelta, timezone, datetime
import FormatData
import ConvertToReadable
import OffsetLoop
import fetch_json
import Translate
class TestLastSeen(unittest.TestCase):

    def test_True(self):
        result = ConvertToReadable.ConvertToReadable({"user":True},"1")
        self.assertEqual(result, "User " + "user" + " is online")

        result2 = ConvertToReadable.ConvertToReadable({"user":True}, "2")
        self.assertEqual(result2, "Користувач " + "user" + " онлайн")


    def test_CoupleOfMinutes(self):
        result = ConvertToReadable.ConvertToReadable({"user":timedelta(hours=0, minutes=16, seconds=59, microseconds=384718)},"1")
        self.assertEqual(result, "User " + "user"+ " was last seen at " + "0:16:59.384718" + " (couple of minutes ago)")

        result2 = ConvertToReadable.ConvertToReadable({"user":timedelta(hours=0, minutes=16, seconds=59, microseconds=384718)},"2")
        self.assertEqual(result2, "Користувач " + "user"+ " в останнє був присутній " + "0:16:59.384718" + " (декілька хвилин тому)")
    def test_LessThenMinutes(self):
        result = ConvertToReadable.ConvertToReadable({"user":timedelta(hours=0, minutes=0, seconds=30, microseconds=384718)},"1")
        self.assertEqual(result,"User " + "user" + " was last seen at " + "0:00:30.384718" + " (less than a minute ago)")

        result2 = ConvertToReadable.ConvertToReadable({"user":timedelta(hours=0, minutes=0, seconds=30, microseconds=384718)}, "2")
        self.assertEqual(result2,"Користувач " + "user" + " в останнє був присутній " + "0:00:30.384718" + " (менше хвилини тому)")


    def test_Yesterday(self):
        result = ConvertToReadable.ConvertToReadable({"user":timedelta(days=1, hours=1, minutes=0, seconds=30, microseconds=384718)},"1")
        self.assertEqual(result,"User " + "user" + " was last seen at " + "1 day, 1:00:30.384718" + " (yesterday)")

        result2 = ConvertToReadable.ConvertToReadable({"user":timedelta(days=1, hours=1, minutes=0, seconds=30, microseconds=384718)}, "2")
        self.assertEqual(result2,"Користувач " + "user" + " в останнє був присутній " + "1 day, 1:00:30.384718" + " (вчора)")


    def test_Hour(self):
        result = ConvertToReadable.ConvertToReadable({"user":timedelta(days=0, hours=1, minutes=0, seconds=30, microseconds=384718)},"1")
        self.assertEqual(result,"User " + "user" + " was last seen at " + "1:00:30.384718" + " (hour ago)")

        result2 = ConvertToReadable.ConvertToReadable({"user":timedelta(days=0, hours=1, minutes=0, seconds=30, microseconds=384718)},"2")
        self.assertEqual(result2,"Користувач " + "user" + " в останнє був присутній " + "1:00:30.384718" + " (годину тому)")

    def test_today(self):
        result =ConvertToReadable.ConvertToReadable({"user":timedelta(days=0, hours=2, minutes=0, seconds=59, microseconds=384718)} ,"1")
        self.assertEqual(result,"User " + "user" + " was last seen at " + "2:00:59.384718" + " (today)")

        result2 = ConvertToReadable.ConvertToReadable({"user":timedelta(days=0, hours=2, minutes=0, seconds=59, microseconds=384718)},"2")
        self.assertEqual(result2,"Користувач " + "user" + " в останнє був присутній " + "2:00:59.384718" + " (сьогодні)")

    def test_This_Week(self):
        result =ConvertToReadable.ConvertToReadable({"user":timedelta(days=2, hours=2, minutes=0, seconds=59, microseconds=384718)},"1")
        self.assertEqual(result,"User " + "user" + " was last seen at " + "2 days, 2:00:59.384718" + " (this week)")

        result2 = ConvertToReadable.ConvertToReadable({"user":timedelta(days=2, hours=2, minutes=0, seconds=59, microseconds=384718)},"2")
        self.assertEqual(result2,"Користувач " + "user" + " в останнє був присутній " + "2 days, 2:00:59.384718" + " (цього тижня)")

    def test_LongAgo(self):
        result = ConvertToReadable.ConvertToReadable({"user":timedelta(days=8, hours=2, minutes=0, seconds=59, microseconds=384718)},"1")
        self.assertEqual(result,"User " + "user" + " was last seen at " + "8 days, 2:00:59.384718" + " (Long ago)")

        result2 = ConvertToReadable.ConvertToReadable({"user":timedelta(days=8, hours=2, minutes=0, seconds=59, microseconds=384718)},"2")
        self.assertEqual(result2,"Користувач " + "user" + " в останнє був присутній " + "8 days, 2:00:59.384718" + " (давно)")

    def test_FormatDataOffline(self):
        result = FormatData.FormatData(
            {'userId': '2fba2529-c166-8574-2da2-eac544d82634', 'nickname': 'Doug93', 'firstName': 'Doug',
             'lastName': 'Rogahn', 'registrationDate': '2023-06-04T03:53:45.4490942+00:00',
             'lastSeenDate': '2023-09-24T15:22:42.9695297+00:00', 'isOnline': False})
        self.assertEqual(result, datetime.now().astimezone(timezone.utc) - datetime.fromisoformat(
            "2023-09-24T15:22:42.9695297+00:00"))

    def test_FormatDataOnline(self):
        result =  FormatData.FormatData(
            {'userId': '2fba2529-c166-8574-2da2-eac544d82634', 'nickname': 'Doug93', 'firstName': 'Doug',
             'lastName': 'Rogahn', 'registrationDate': '2023-06-04T03:53:45.4490942+00:00',
             'lastSeenDate': '2023-09-24T15:22:42.9695297+00:00', 'isOnline': True})
        self.assertEqual(result, True)

    def test_GetJason(self):
        result = fetch_json.fetch_json("https://sef.podkolzin.consulting/api/users/lastSeen?offset=0")
        self.assertEqual(result["data"][0]["nickname"], "Doug93")
    def test_GetJason2(self):
        result = fetch_json.fetch_json("https://sef.podkolzin.consulting/api/users/lastSeen?offset=20")
        self.assertEqual(result["data"][0]["nickname"], "Karl94")

    def test_OffsetLoop(self):
        result = OffsetLoop.OffsetLoop()
        self.assertEqual(result[0]["nickname"], "Doug93")

    def test_Translate(self):
        result = Translate.Translate("1")
        self.assertEqual(result, ["User ", " was last seen at ", " (just now)", " (less than a minute ago)", " (couple of minutes ago)",
              " (hour ago)", " (today)", " (yesterday)", " (this week)", " (Long ago)", " is online"])

        result2 = Translate.Translate("2")
        self.assertEqual(result2, ["Користувач ", " в останнє був присутній ", " (тільки що)", " (менше хвилини тому)",
              " (декілька хвилин тому)",
              " (годину тому)", " (сьогодні)", " (вчора)", " (цього тижня)", " (давно)", " онлайн"])


