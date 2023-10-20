import os
import unittest
from unittest.mock import patch
from Functions import main

class E2E210(unittest.TestCase):

    DIR = os.path.dirname(os.path.abspath(__file__))
    csv = os.path.join(DIR, 'Report')

    @patch('builtins.input',
           side_effect=['2', '11',csv,'kk'])
    def test_get_historical_data(self, mock_input):
        result = main.main()
        self.assertEqual(result,['Report Name: kk',
 '2fba2529-c166-8574-2da2-eac544d82634:',
 "[{'min time': 3600.0}, {'max time': 25200.0}, {'dailyAverage': 43200.0}, "
 "{'WeeklyAverage': 43200.0}]",
 '2fba2529-c166-8574-2da2-eac544d826341:',
 "[{'min time': 3600.0}, {'max time': 25200.0}, {'dailyAverage': 43200.0}, "
 "{'WeeklyAverage': 43200.0}]"])