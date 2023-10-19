import unittest

import subprocess

class E2E11(unittest.TestCase):

    @staticmethod
    def Run(command, inputData):
        process = subprocess.Popen(command, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE,text=True)
        stdout = process.communicate(input=inputData)
        return stdout[0]

    def test_e2e_11_Users(self):
        input = "1\n1\n"
        output = self.Run(["python", "../Functions/main.py"], input)
        lines = output.split('\n')
        Normal=False
        if 'Nathaniel6' in lines[2]:
            Normal = True
        print(output)
        self.assertEqual(Normal, True)



