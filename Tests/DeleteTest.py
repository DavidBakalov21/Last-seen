
import Functions.DeleteUser
import unittest
class TestDelete(unittest.TestCase):

    def test_Delete_NormId_WasDone(self):
        result = Functions.DeleteUser.DeleteData('DelTest.csv', '2fba2529-c166-8574-2da2-eac544d82634')
        self.assertEqual(result,'it was done')
    def test_Delete_BadId_NotDone(self):
        result = Functions.DeleteUser.DeleteData('DelTest.csv', '2fba2529-c166-8sashjkd574-2da2-easdfgc544d82634')
        self.assertEqual(result, "user wasn't present or id was incorect")