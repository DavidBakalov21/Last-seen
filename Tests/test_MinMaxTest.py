import Functions.MinMax
import unittest
class MinMaxTest(unittest.TestCase):

    def test_Max_NormId_25200(self):
        result = Functions.MinMax.Max('outputF1.csv', '2fba2529-c166-8574-2da2-eac544d82634')
        self.assertEqual(result, {'max time': 25200.0})

    def test_Min_NormId_7200(self):
        result = Functions.MinMax.Min('outputF1.csv', '2fba2529-c166-8574-2da2-eac544d82634')
        self.assertEqual(result, {'min time': 7200.0})
    def test_Min_BadId_BadId(self):
        result = Functions.MinMax.Min('outputF1.csv', '2fba2529-c166-8574-2da2-easdfgc544d82634')
        self.assertEqual(result, 'ID is wrong')
    def test_Max_BadId_BadId(self):
        result = Functions.MinMax.Max('outputF1.csv', '2fba2529-c166-8574-2da2-easdfgc544d82634')
        self.assertEqual(result, 'ID is wrong')
