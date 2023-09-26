
import unittest
from unittest.mock import patch
from Functions.OffsetLoop import OffsetLoop

class TestOffsetLoop(unittest.TestCase):

    @patch('Functions.OffsetLoop.fetch_json')
    def test_OffsetLoop_FirstTwoNicknames_Doug93AndKarl94(self, MockGet):
        MockGet.side_effect = [
            {"data": [{"nickname": "Doug93"}, {"nickname": "Karl94"}]}, {"data": []}]
        result = OffsetLoop()
        self.assertEqual(result, [{"nickname": "Doug93"}, {"nickname": "Karl94"}])