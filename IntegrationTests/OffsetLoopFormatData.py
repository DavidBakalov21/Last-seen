import unittest
from unittest.mock import patch
from datetime import timezone, datetime
from Functions.OffsetLoop import OffsetLoop
from Functions.FormatData import FormatData
class OffsetLoopFormatData(unittest.TestCase):

    @patch('Functions.OffsetLoop.fetch_json')
    def test_OffsetLoopFormatData_Doug93isOnlineFalse_DatetimeMinusTime(self, MockGet):
        MockGet.side_effect = [
            {"data": [{"nickname": "Doug93",'userId':"212","lastSeenDate":'2023-09-24T15:22:42.9695297+00:00', 'isOnline': False}]}, {"data": []}]
        resultOffset = OffsetLoop()
        #self.assertEqual(result, [{"nickname": "Doug93","lastSeenDate":'2023-09-24T15:22:42.9695297+00:00', 'isOnline': False}])

        result = FormatData(
            resultOffset[0])
        self.assertEqual(result, datetime.now().astimezone(timezone.utc) - datetime.fromisoformat(
            "2023-09-24T15:22:42.9695297+00:00"))

    @patch('Functions.OffsetLoop.fetch_json')
    def test_OffsetLoopFormatData_Doug93isOnlineTrue_True(self, MockGet):
        MockGet.side_effect = [
            {"data": [{"nickname": "Doug93",'userId':"212", "lastSeenDate": '2023-09-24T15:22:42.9695297+00:00', 'isOnline': True}]},
            {"data": []}]
        resultOffset = OffsetLoop()
        # self.assertEqual(result, [{"nickname": "Doug93","lastSeenDate":'2023-09-24T15:22:42.9695297+00:00', 'isOnline': False}])

        result = FormatData(
            resultOffset[0])
        self.assertEqual(result, True)


