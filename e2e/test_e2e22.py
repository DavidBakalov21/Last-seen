import os
import unittest
from unittest.mock import patch
from Functions import main

class E2E22(unittest.TestCase):

    DIR = os.path.dirname(os.path.abspath(__file__))
    csv = os.path.join(DIR, 'GetDataForUser.csv')

    @patch('builtins.input', side_effect=['2', '2', csv, '04-10-2023 18:56', '8c417d9d-b13f-f070-bf07-1fd9c768126f'])
    def test_get_historical_data(self, mock_input):
        result = main.main()
        self.assertEqual(result, {'wasUserOnline': False, 'nearestOnlineTime': '04-10-2023 18:59'})