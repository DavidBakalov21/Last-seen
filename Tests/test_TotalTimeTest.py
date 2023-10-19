import Functions.TotalTime
import unittest
class TestTotalTime(unittest.TestCase):

    def test_TimeTotal_NormId_32400(self):
        result = Functions.TotalTime.TotalTime('outputF1.csv', '2fba2529-c166-8574-2da2-eac544d82634')
        self.assertEqual(result, {'totalTime': 32400.0})
    def test_TimeTotal_BadId_BadId(self):
        result = Functions.TotalTime.TotalTime('outputF1.csv', '2fba2529-c166-8574-2da2-easdfgc544d82634')
        self.assertEqual(result, 'ID is wrong')

