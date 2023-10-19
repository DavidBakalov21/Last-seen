from datetime import timezone, datetime
import unittest
from Functions.FormatData import FormatData
class TestFormatData(unittest.TestCase):

    def test_FormatData_LastSeen_CurrentTimeMinusLastSeen(self):
        result = FormatData(
            {'userId': '2fba2529-c166-8574-2da2-eac544d82634', 'nickname': 'Doug93', 'firstName': 'Doug',
             'lastName': 'Rogahn', 'registrationDate': '2023-06-04T03:53:45.4490942+00:00',
             'lastSeenDate': '2023-09-24T15:22:42.9695297+00:00', 'isOnline': False})
        self.assertEqual(result, datetime.now().astimezone(timezone.utc) - datetime.fromisoformat(
            "2023-09-24T15:22:42.9695297+00:00"))

    def test_FormatData_Online_True(self):
        result = FormatData(
            {'userId': '2fba2529-c166-8574-2da2-eac544d82634', 'nickname': 'Doug93', 'firstName': 'Doug',
             'lastName': 'Rogahn', 'registrationDate': '2023-06-04T03:53:45.4490942+00:00',
             'lastSeenDate': '2023-09-24T15:22:42.9695297+00:00', 'isOnline': True})
        self.assertEqual(result, True)
