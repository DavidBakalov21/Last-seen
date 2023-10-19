import unittest

import subprocess
class E2E3(unittest.TestCase):

    @staticmethod
    def Run(command, inputData):
        process = subprocess.Popen(command, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        stdout = process.communicate(input=inputData)
        return stdout[0]

    def test_e2e_3IncorectId_Incorect(self):
        input = "3\nGetDataTest\n'8c417d9d-b13f-f070-bf07-1fd9sdscscc768126fvg'\n"
        output = self.Run(["python", "../Functions/main.py"], input)
        lines = output.split('\n')
        print(output)
        self.assertEqual(lines[len(lines)-2], "user wasn't present or id was incorect")