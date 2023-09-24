import unittest
import main
from datetime import timedelta


class TestLastSeen(unittest.TestCase):

    def test_True(self):
        result = main.ConvertToReadable(True, "user","1")
        self.assertEqual(result, "User " + "user" + " is online")

        result2 = main.ConvertToReadable(True, "user", "2")
        self.assertEqual(result2, "Користувач " + "user" + " онлайн")


    def test_CoupleOfMinutes(self):
        result = main.ConvertToReadable(timedelta(hours=0, minutes=16, seconds=59, microseconds=384718), "user","1")
        self.assertEqual(result, "User " + "user"+ " was last seen at " + "0:16:59.384718" + " (couple of minutes ago)")

    def test_LessThenMinutes(self):
        result = main.ConvertToReadable(timedelta(hours=0, minutes=0, seconds=30, microseconds=384718), "user","1")
        self.assertEqual(result,"User " + "user" + " was last seen at " + "0:00:30.384718" + " (less than a minute ago)")
    def test_Yesterday(self):
        result = main.ConvertToReadable(timedelta(days=1, hours=1, minutes=0, seconds=30, microseconds=384718), "user","1")
        self.assertEqual(result,"User " + "user" + " was last seen at " + "1 day, 1:00:30.384718" + " (yesterday)")

    def test_Hour(self):
        result = main.ConvertToReadable(timedelta(days=0, hours=1, minutes=0, seconds=30, microseconds=384718), "user","1")
        self.assertEqual(result,"User " + "user" + " was last seen at " + "1:00:30.384718" + " (hour ago)")
    def test_today(self):
        result = main.ConvertToReadable(timedelta(days=0, hours=2, minutes=0, seconds=59, microseconds=384718), "user","1")
        self.assertEqual(result,"User " + "user" + " was last seen at " + "2:00:59.384718" + " (today)")

    def test_This_Week(self):
        result = main.ConvertToReadable(timedelta(days=2, hours=2, minutes=0, seconds=59, microseconds=384718), "user","1")
        self.assertEqual(result,"User " + "user" + " was last seen at " + "2 days, 2:00:59.384718" + " (this week)")

    def test_LongAgo(self):
        result = main.ConvertToReadable(timedelta(days=8, hours=2, minutes=0, seconds=59, microseconds=384718), "user","1")
        self.assertEqual(result,"User " + "user" + " was last seen at " + "8 days, 2:00:59.384718" + " (Long ago)")
    # Using unittest's assertion method

