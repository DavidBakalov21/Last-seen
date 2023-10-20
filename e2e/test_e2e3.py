import os
import unittest
from unittest.mock import patch
from Functions import main
class E2E3(unittest.TestCase):
    DIR = os.path.dirname(os.path.abspath(__file__))
    csv = os.path.join(DIR, 'GetDataTest')
    @patch('builtins.input', side_effect=['3',csv, '8c417d9d-b13f-f070-bf07-1fd9sdscscc768126fvg'])
    def test_get_historical_data(self, mock_input):
        result = main.main()
        #This is fixed test
        # This is fixed test
        # This is fixed test
        self.assertEqual(result, "user wasn't present or id was incorect")