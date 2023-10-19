import unittest

import subprocess

class E2E21(unittest.TestCase):

    @staticmethod
    def Run(command, inputData):
        process = subprocess.Popen(command, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        stdout = process.communicate(input=inputData)
        return stdout[0]

    def test_e2e_21_Users(self):
        input = "2\n1\nGetDataTest\n04-10-2023 18:45\n"
        output = self.Run(["python", "../Functions/main.py"], input)
        lines = output.split('\n')
        #print(output)
        self.assertEqual(lines[len(lines)-2], "{'usersOnline': 2}")