import os
import unittest
from unittest.mock import patch
from Functions import main

class E2E27(unittest.TestCase):



    DIR = os.path.dirname(os.path.abspath(__file__))
    csv = os.path.join(DIR, 'outputRange.csv')

    @patch('builtins.input',
           side_effect=['2', '7', csv, '2023-10-10T17:25:41.988544+00:00','2023-10-11T20:21:41.988544+00:00','2fba2529-c166-8574-2da2-eac544d82634'])
    def test_get_historical_data(self, mock_input):
        result = main.main()
        self.assertEqual(result, {'totalTime': 32400.0})