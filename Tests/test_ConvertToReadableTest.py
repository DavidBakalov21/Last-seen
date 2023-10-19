import unittest
from datetime import timedelta
from Functions.ConvertToReadable import ConvertToReadable


class TestConvertToReadable(unittest.TestCase):

    def test_ConvertToReadable_UserIsOnline_IsOnline(self):
        result = ConvertToReadable({"user": True}, "1")
        self.assertEqual(result, "User " + "user" + " is online")
        result2 = ConvertToReadable({"user": True}, "2")
        self.assertEqual(result2, "Користувач " + "user" + " онлайн")

    def test_ConvertToReadable_16Minutes59Seconds_CoupleOfMinutes(self):
        result = ConvertToReadable(
            {"user": timedelta(hours=0, minutes=16, seconds=59, microseconds=384718)}, "1")
        self.assertEqual(result,
                         "User " + "user" + " was last seen at " + "0:16:59.384718" + " (couple of minutes ago)")
        result2 = ConvertToReadable(
            {"user": timedelta(hours=0, minutes=16, seconds=59, microseconds=384718)}, "2")
        self.assertEqual(result2,
                         "Користувач " + "user" + " в останнє був присутній " + "0:16:59.384718" + " (декілька хвилин тому)")

    def test_ConvertToReadable_30Seconds_LessThenMinute(self):
        result = ConvertToReadable(
            {"user": timedelta(hours=0, minutes=0, seconds=30, microseconds=384718)}, "1")
        self.assertEqual(result,
                         "User " + "user" + " was last seen at " + "0:00:30.384718" + " (less than a minute ago)")
        result2 = ConvertToReadable(
            {"user": timedelta(hours=0, minutes=0, seconds=30, microseconds=384718)}, "2")
        self.assertEqual(result2,
                         "Користувач " + "user" + " в останнє був присутній " + "0:00:30.384718" + " (менше хвилини тому)")

    def test_ConvertToReadable_1Day1Hour30Seconds_Yesterday(self):
        result = ConvertToReadable(
            {"user": timedelta(days=1, hours=1, minutes=0, seconds=30, microseconds=384718)}, "1")
        self.assertEqual(result, "User " + "user" + " was last seen at " + "1 day, 1:00:30.384718" + " (yesterday)")
        result2 = ConvertToReadable(
            {"user": timedelta(days=1, hours=1, minutes=0, seconds=30, microseconds=384718)}, "2")
        self.assertEqual(result2,
                         "Користувач " + "user" + " в останнє був присутній " + "1 day, 1:00:30.384718" + " (вчора)")

    def test_ConvertToReadable_1Hour30Seconds_HourAgo(self):
        result = ConvertToReadable(
            {"user": timedelta(days=0, hours=1, minutes=0, seconds=30, microseconds=384718)}, "1")
        self.assertEqual(result, "User " + "user" + " was last seen at " + "1:00:30.384718" + " (hour ago)")
        result2 = ConvertToReadable(
            {"user": timedelta(days=0, hours=1, minutes=0, seconds=30, microseconds=384718)}, "2")
        self.assertEqual(result2,
                         "Користувач " + "user" + " в останнє був присутній " + "1:00:30.384718" + " (годину тому)")

    def test_ConvertToReadable_2Hours59Seconds_today(self):
        result = ConvertToReadable(
            {"user": timedelta(days=0, hours=2, minutes=0, seconds=59, microseconds=384718)}, "1")
        self.assertEqual(result, "User " + "user" + " was last seen at " + "2:00:59.384718" + " (today)")
        result2 = ConvertToReadable(
            {"user": timedelta(days=0, hours=2, minutes=0, seconds=59, microseconds=384718)}, "2")
        self.assertEqual(result2,
                         "Користувач " + "user" + " в останнє був присутній " + "2:00:59.384718" + " (сьогодні)")

    def test_ConvertToReadable_2Days2Hours59Seconds_ThisWeek(self):
        result = ConvertToReadable(
            {"user": timedelta(days=2, hours=2, minutes=0, seconds=59, microseconds=384718)}, "1")
        self.assertEqual(result, "User " + "user" + " was last seen at " + "2 days, 2:00:59.384718" + " (this week)")
        result2 = ConvertToReadable(
            {"user": timedelta(days=2, hours=2, minutes=0, seconds=59, microseconds=384718)}, "2")
        self.assertEqual(result2,
                         "Користувач " + "user" + " в останнє був присутній " + "2 days, 2:00:59.384718" + " (цього тижня)")

    def test_ConvertToReadable_8Days2Hours59Seconds_LongAgo(self):
        result = ConvertToReadable(
            {"user": timedelta(days=8, hours=2, minutes=0, seconds=59, microseconds=384718)}, "1")
        self.assertEqual(result, "User " + "user" + " was last seen at " + "8 days, 2:00:59.384718" + " (Long ago)")
        result2 = ConvertToReadable(
            {"user": timedelta(days=8, hours=2, minutes=0, seconds=59, microseconds=384718)}, "2")
        self.assertEqual(result2,
                         "Користувач " + "user" + " в останнє був присутній " + "8 days, 2:00:59.384718" + " (давно)")
