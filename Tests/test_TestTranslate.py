
import unittest
from Functions.Translate import  Translate
class TestTranslate(unittest.TestCase):

    def test_Translate_1_EnglishString(self):
        result = Translate("1")
        self.assertEqual(result, ["User ", " was last seen at ", " (just now)", " (less than a minute ago)",
                                  " (couple of minutes ago)",
                                  " (hour ago)", " (today)", " (yesterday)", " (this week)", " (Long ago)",
                                  " is online"])

    def test_Translate_2_UkrainianString(self):
        result2 = Translate("2")
        self.assertEqual(result2, ["Користувач ", " в останнє був присутній ", " (тільки що)", " (менше хвилини тому)",
                                   " (декілька хвилин тому)",
                                   " (годину тому)", " (сьогодні)", " (вчора)", " (цього тижня)", " (давно)",
                                   " онлайн"])