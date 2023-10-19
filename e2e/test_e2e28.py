import os
import unittest
from unittest.mock import patch
from Functions import main
class E2E28(unittest.TestCase):


    DIR = os.path.dirname(os.path.abspath(__file__))
    csv = os.path.join(DIR, 'outputF1.csv')

    @patch('builtins.input',
           side_effect=['2', '8', csv, '2fba2529-c166-8574-2da2-eac544d82634'])
    def test_get_historical_data(self, mock_input):
        result = main.main()
        self.assertEqual(result, {'min time': 7200.0})