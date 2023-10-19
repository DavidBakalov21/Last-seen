import os
import unittest
from unittest.mock import patch
from Functions import main

class E2E24(unittest.TestCase):


    DIR = os.path.dirname(os.path.abspath(__file__))
    csv = os.path.join(DIR, 'UserPredictTest.csv')

    @patch('builtins.input', side_effect=['2', '4', csv, '27-10-2023 18:45','8c417d9d-b13f-f070-bf07-1fd9c768126f',0.74])
    def test_get_historical_data(self, mock_input):
        result = main.main()
        self.assertEqual(result, {'willBeOnline': True, 'onlineChance': 0.75})