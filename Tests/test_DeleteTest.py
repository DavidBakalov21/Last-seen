import os

import Functions.DeleteUser
import unittest
class TestDelete(unittest.TestCase):
    DIR = os.path.dirname(os.path.abspath(__file__))
    def test_Delete_NormId_WasDone(self):
        csv = os.path.join(TestDelete.DIR, 'DelTest.csv')
        result = Functions.DeleteUser.DeleteData(csv, '2fba2529-c166-8574-2da2-eac544d82634')
        self.assertEqual(result,'it was done')
    def test_Delete_BadId_NotDone(self):
        csv = os.path.join(TestDelete.DIR, 'DelTest.csv')
        result = Functions.DeleteUser.DeleteData(csv, '2fba2529-c166-8sashjkd574-2da2-easdfgc544d82634')
        self.assertEqual(result, "user wasn't present or id was incorect")