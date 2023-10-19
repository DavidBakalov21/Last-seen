import unittest

import subprocess

class E2E25(unittest.TestCase):

    @staticmethod
    def Run(command, inputData):
        process = subprocess.Popen(command, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE,text=True)
        stdout = process.communicate(input=inputData)
        return stdout[0]

    def test_e2e_25_32400(self):
        input = "2\n5\noutputF1.csv\n2fba2529-c166-8574-2da2-eac544d82634\n"
        output= self.Run(["python", "../Functions/main.py"], input)
        lines = output.split('\n')
        print(output)
        self.assertEqual(lines[4], "{'totalTime': 32400.0}")