import unittest
from unittest.mock import patch, Mock
from Functions.fetch_json import fetch_json
class Test_fetch_json(unittest.TestCase):
    @patch('requests.get')
    def test_fetch_json_Offest0_Doug93(self, MockGet):
        mock_response = Mock()
        mock_response.json.return_value = {"data": [{"nickname": "Doug93"}]}
        MockGet.return_value = mock_response
        result = fetch_json("https://sef.podkolzin.consulting/api/users/lastSeen?offset=0")
        self.assertEqual(result["data"][0]["nickname"], "Doug93")

    @patch('requests.get')
    def test_fetch_json_Offest20_Karl94(self, MockGet):
        mock_response = Mock()
        mock_response.json.return_value = {"data": [{"nickname": "Karl94"}]}
        MockGet.return_value = mock_response
        result = fetch_json("https://sef.podkolzin.consulting/api/users/lastSeen?offset=20")
        self.assertEqual(result["data"][0]["nickname"], "Karl94")