
from Functions.FormatData import FormatData
import unittest
from datetime import timedelta
from Functions.ConvertToReadable import ConvertToReadable


class TestConvertToReadable(unittest.TestCase):

    def test_FromatDataConvertToReadable_UserIsOnline_IsOnline(self):
        resultF = FormatData(
            {'userId': '2fba2529-c166-8574-2da2-eac544d82634', 'nickname': 'Doug93', 'firstName': 'Doug',
             'lastName': 'Rogahn', 'registrationDate': '2023-06-04T03:53:45.4490942+00:00',
             'lastSeenDate': '2023-09-24T15:22:42.9695297+00:00', 'isOnline': True})

        result = ConvertToReadable({"user": resultF}, "1")
        self.assertEqual(result, "User " + "user" + " is online")
        result2 = ConvertToReadable({"user": resultF}, "2")
        self.assertEqual(result2, "Користувач " + "user" + " онлайн")


#Because of test using real time it might give an error, but the difference between "24 days, 19:22:05.421734" and current result will show us that everything works okay
    def test_ConvertToReadable_24Days22Hours_LongAgo(self):
        resultF = FormatData(
            {'userId': '2fba2529-c166-8574-2da2-eac544d82634', 'nickname': 'Doug93', 'firstName': 'Doug',
             'lastName': 'Rogahn', 'registrationDate': '2023-06-04T03:53:45.4490942+00:00',
             'lastSeenDate': '2023-09-12T15:22:42.9695297+00:00', 'isOnline': False})

        result = ConvertToReadable(
            {"user": resultF}, "1")
        self.assertEqual(result, "User " + "user" + " was last seen at " + "24 days, 19:22:05.421734" + " (Long ago)")
        result2 = ConvertToReadable(
            {"user": resultF}, "2")
        self.assertEqual(result2,
                         "Користувач " + "user" + " в останнє був присутній " + "24 days, 19:22:05.421734" + " (давно)")