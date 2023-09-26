
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

    @patch('Functions.OffsetLoop.fetch_json')
    def test_OffsetLoop_DefferentNumberOfItems_Doug93AndKarl94(self, MockGet):
        MockGet.side_effect = [
            {"data": [{"nickname": "Doug93"}, {"nickname": "Karl94"}]},
            {"data": [{"nickname": "Doug993"}]},
            {"data": [{"nickname": "Doug193"}, {"nickname": "Doug1033"}, {"nickname": "Karl994"}]},
            {"data": []}]
        result = OffsetLoop()
        self.assertEqual(result, [{"nickname": "Doug93"}, {"nickname": "Karl94"},{"nickname": "Doug993"},{"nickname": "Doug193"},{"nickname": "Doug1033"}, {"nickname": "Karl994"}])

    @patch('Functions.OffsetLoop.fetch_json')
    def test_OffsetLoop_Empty_Doug93AndKarl94(self, MockGet):
        MockGet.side_effect = [

            {"data": []}]
        result = OffsetLoop()
        self.assertEqual(result, [])

    @patch('Functions.OffsetLoop.fetch_json')
    def test_OffsetLoop_TwoFullPages_Doug93AndKarl94(self, MockGet):
        MockGet.side_effect = [

            {"data":  [{"nickname": "Doug93"}, {"nickname": "Karl94"}, {"nickname": "Karl94"}, {"nickname": "Karl94"},
                      {"nickname": "Karl94"}, {"nickname": "Karl94"}, {"nickname": "Karl94"}, {"nickname": "Karl94"},
                      {"nickname": "Karl94"}, {"nickname": "Karl94"}, {"nickname": "Karl94"}, {"nickname": "Karl94"},
                      {"nickname": "Karl94"}, {"nickname": "Karl94"}, {"nickname": "Karl94"}, {"nickname": "Karl94"},
                      {"nickname": "Karl94"}, {"nickname": "Karl94"}, {"nickname": "Karl94"}, {"nickname": "Karl94"}]},

            {"data": [{"nickname": "Doug93"}, {"nickname": "Karl94"}, {"nickname": "Karl94"}, {"nickname": "Karl94"},
                      {"nickname": "Karl94"}, {"nickname": "Karl94"}, {"nickname": "Karl94"}, {"nickname": "Karl94"},
                      {"nickname": "Karl94"}, {"nickname": "Karl94"}, {"nickname": "Karl94"}, {"nickname": "Karl94"},
                      {"nickname": "Karl94"}, {"nickname": "Karl94"}, {"nickname": "Karl94"}, {"nickname": "Karl94"},
                      {"nickname": "Karl94"}, {"nickname": "Karl94"}, {"nickname": "Karl94"}, {"nickname": "Karl94"}]},

            {"data": []}]

        result = OffsetLoop()
        self.assertEqual(result, [{"nickname": "Doug93"}, {"nickname": "Karl94"}, {"nickname": "Karl94"}, {"nickname": "Karl94"},
                      {"nickname": "Karl94"}, {"nickname": "Karl94"}, {"nickname": "Karl94"}, {"nickname": "Karl94"},
                      {"nickname": "Karl94"}, {"nickname": "Karl94"}, {"nickname": "Karl94"}, {"nickname": "Karl94"},
                      {"nickname": "Karl94"}, {"nickname": "Karl94"}, {"nickname": "Karl94"}, {"nickname": "Karl94"},
                      {"nickname": "Karl94"}, {"nickname": "Karl94"}, {"nickname": "Karl94"}, {"nickname": "Karl94"},{"nickname": "Doug93"}, {"nickname": "Karl94"}, {"nickname": "Karl94"}, {"nickname": "Karl94"},
                      {"nickname": "Karl94"}, {"nickname": "Karl94"}, {"nickname": "Karl94"}, {"nickname": "Karl94"},
                      {"nickname": "Karl94"}, {"nickname": "Karl94"}, {"nickname": "Karl94"}, {"nickname": "Karl94"},
                      {"nickname": "Karl94"}, {"nickname": "Karl94"}, {"nickname": "Karl94"}, {"nickname": "Karl94"},
                      {"nickname": "Karl94"}, {"nickname": "Karl94"}, {"nickname": "Karl94"}, {"nickname": "Karl94"}])