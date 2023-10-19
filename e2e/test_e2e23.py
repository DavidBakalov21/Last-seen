import os
import unittest
from unittest.mock import patch
from Functions import main
class E2E23(unittest.TestCase):


    DIR = os.path.dirname(os.path.abspath(__file__))
    csv = os.path.join(DIR, 'GetDataForUser.csv')

    @patch('builtins.input', side_effect=['2', '3', csv, '03-11-2023 18:45'])
    def test_get_historical_data(self, mock_input):
        result = main.main()
        self.assertEqual(result, 4)