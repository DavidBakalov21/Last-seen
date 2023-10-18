import unittest

import subprocess

class E2E27(unittest.TestCase):

    @staticmethod
    def Run(command, inputData):
        process = subprocess.Popen(command, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE,text=True)
        stdout = process.communicate(input=inputData)
        return stdout[0]

    def test_e2e_27_TimeOnRange(self):
        input = "2\n7\noutputRange.csv\n2023-10-10T17:25:41.988544+00:00\n2023-10-11T20:21:41.988544+00:00\n2fba2529-c166-8574-2da2-eac544d82634\n"
        output = self.Run(["python", "../Functions/main.py"], input)
        lines = output.split('\n')
        print(output)
        self.assertEqual(lines[6], "{'totalTime': 32400.0}")