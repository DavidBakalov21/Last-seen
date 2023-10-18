import unittest

import subprocess

class E2E29(unittest.TestCase):

    @staticmethod
    def Run(command, inputData):
        process = subprocess.Popen(command, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE,text=True)
        stdout = process.communicate(input=inputData)
        return stdout[0]

    def test_e2e_29_Max(self):
        input = "2\n9\noutputF1.csv\n2fba2529-c166-8574-2da2-eac544d82634\n"
        output = self.Run(["python", "../Functions/main.py"], input)
        lines = output.split('\n')
        print(output)
        self.assertEqual(lines[4], "{'max time': 25200.0}")