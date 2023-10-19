
from Functions.FormatData import FormatData
import unittest

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


