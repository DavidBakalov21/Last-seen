
import unittest
from unittest.mock import patch
from Functions.OffsetLoop import OffsetLoop

class TestOffsetLoop(unittest.TestCase):

    @patch('Functions.OffsetLoop.fetch_json')
    def test_OffsetLoop_FirstTwoNicknames_Doug93AndKarl94(self, MockGet):
        MockGet.side_effect = [
            {"data": [{"nickname": "Doug93", 'userId':"212"}, {"nickname": "Karl94",'userId':"212"}]}, {"data": []}]
        result = OffsetLoop()
        self.assertEqual(result, [{"nickname": "Doug93",'userId':"212"}, {"nickname": "Karl94",'userId':"212"}])

    @patch('Functions.OffsetLoop.fetch_json')
    def test_OffsetLoop_DefferentNumberOfItems_Doug93AndKarl94(self, MockGet):
        MockGet.side_effect = [
            {"data": [{"nickname": "Doug93",'userId':"212"}, {"nickname": "Karl94",'userId':"212"}]},
            {"data": [{"nickname": "Doug993",'userId':"212"}]},
            {"data": [{"nickname": "Doug193",'userId':"212"}, {"nickname": "Doug1033",'userId':"212"}, {"nickname": "Karl994",'userId':"212"}]},
            {"data": []}]
        result = OffsetLoop()
        self.assertEqual(result, [{"nickname": "Doug93",'userId':"212"}, {"nickname": "Karl94",'userId':"212"},{"nickname": "Doug993",'userId':"212"},{"nickname": "Doug193",'userId':"212"},{"nickname": "Doug1033",'userId':"212"}, {"nickname": "Karl994",'userId':"212"}])

    @patch('Functions.OffsetLoop.fetch_json')
    def test_OffsetLoop_Empty_Doug93AndKarl94(self, MockGet):
        MockGet.side_effect = [

            {"data": []}]
        result = OffsetLoop()
        self.assertEqual(result, [])

    @patch('Functions.OffsetLoop.fetch_json')
    def test_OffsetLoop_TwoFullPages_Doug93AndKarl94(self, MockGet):
        MockGet.side_effect = [

            {"data":  [{"nickname": "Doug93",'userId':"212"}, {"nickname": "Karl94",'userId':"212"}, {"nickname": "Karl94",'userId':"212"}, {"nickname": "Karl94",'userId':"212"},
                      {"nickname": "Karl94",'userId':"212"}, {"nickname": "Karl94",'userId':"212"}, {"nickname": "Karl94",'userId':"212"}, {"nickname": "Karl94",'userId':"212"},
                      {"nickname": "Karl94",'userId':"212"}, {"nickname": "Karl94",'userId':"212"}, {"nickname": "Karl94",'userId':"212"}, {"nickname": "Karl94",'userId':"212"},
                      {"nickname": "Karl94",'userId':"212"}, {"nickname": "Karl94",'userId':"212"}, {"nickname": "Karl94",'userId':"212"}, {"nickname": "Karl94",'userId':"212"},
                      {"nickname": "Karl94",'userId':"212"}, {"nickname": "Karl94",'userId':"212"}, {"nickname": "Karl94",'userId':"212"}, {"nickname": "Karl94",'userId':"212"}]},

            {"data": [{"nickname": "Doug93",'userId':"212"}, {"nickname": "Karl94",'userId':"212"}, {"nickname": "Karl94",'userId':"212"}, {"nickname": "Karl94",'userId':"212"},
                      {"nickname": "Karl94",'userId':"212"}, {"nickname": "Karl94",'userId':"212"}, {"nickname": "Karl94",'userId':"212"}, {"nickname": "Karl94",'userId':"212"},
                      {"nickname": "Karl94",'userId':"212"}, {"nickname": "Karl94",'userId':"212"}, {"nickname": "Karl94",'userId':"212"}, {"nickname": "Karl94",'userId':"212"},
                      {"nickname": "Karl94",'userId':"212"}, {"nickname": "Karl94",'userId':"212"}, {"nickname": "Karl94",'userId':"212"}, {"nickname": "Karl94",'userId':"212"},
                      {"nickname": "Karl94",'userId':"212"}, {"nickname": "Karl94",'userId':"212"}, {"nickname": "Karl94",'userId':"212"}, {"nickname": "Karl94",'userId':"212"}]},

            {"data": []}]

        result = OffsetLoop()
        self.assertEqual(result, [{"nickname": "Doug93",'userId':"212"}, {"nickname": "Karl94",'userId':"212"}, {"nickname": "Karl94",'userId':"212"}, {"nickname": "Karl94",'userId':"212"},
                      {"nickname": "Karl94",'userId':"212"}, {"nickname": "Karl94",'userId':"212"}, {"nickname": "Karl94",'userId':"212"}, {"nickname": "Karl94",'userId':"212"},
                      {"nickname": "Karl94",'userId':"212"}, {"nickname": "Karl94",'userId':"212"}, {"nickname": "Karl94",'userId':"212"}, {"nickname": "Karl94",'userId':"212"},
                      {"nickname": "Karl94",'userId':"212"}, {"nickname": "Karl94",'userId':"212"}, {"nickname": "Karl94",'userId':"212"}, {"nickname": "Karl94",'userId':"212"},
                      {"nickname": "Karl94",'userId':"212"}, {"nickname": "Karl94",'userId':"212"}, {"nickname": "Karl94",'userId':"212"}, {"nickname": "Karl94",'userId':"212"},{"nickname": "Doug93",'userId':"212"}, {"nickname": "Karl94",'userId':"212"}, {"nickname": "Karl94",'userId':"212"}, {"nickname": "Karl94",'userId':"212"},
                      {"nickname": "Karl94",'userId':"212"}, {"nickname": "Karl94",'userId':"212"}, {"nickname": "Karl94",'userId':"212"}, {"nickname": "Karl94",'userId':"212"},
                      {"nickname": "Karl94",'userId':"212"}, {"nickname": "Karl94",'userId':"212"}, {"nickname": "Karl94",'userId':"212"}, {"nickname": "Karl94",'userId':"212"},
                      {"nickname": "Karl94",'userId':"212"}, {"nickname": "Karl94",'userId':"212"}, {"nickname": "Karl94",'userId':"212"}, {"nickname": "Karl94",'userId':"212"},
                      {"nickname": "Karl94",'userId':"212"}, {"nickname": "Karl94",'userId':"212"}, {"nickname": "Karl94",'userId':"212"}, {"nickname": "Karl94",'userId':"212"}])