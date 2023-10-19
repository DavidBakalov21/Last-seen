import unittest

import subprocess

class E2E24(unittest.TestCase):

    @staticmethod
    def Run(command, inputData):
        process = subprocess.Popen(command, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE,text=True)
        stdout = process.communicate(input=inputData)
        return stdout[0]

    def test_e2e_24_True(self):
        input = "2\n4\nUserPredictTest.csv\n27-10-2023 18:45\n8c417d9d-b13f-f070-bf07-1fd9c768126f\n0.74\n"
        output = self.Run(["python", "../Functions/main.py"], input)
        lines = output.split('\n')
        #print(output)
        self.assertEqual(lines[len(lines)-2], "{'willBeOnline': True, 'onlineChance': 0.75}")