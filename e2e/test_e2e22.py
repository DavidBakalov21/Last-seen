import unittest

import subprocess

class E2E22(unittest.TestCase):

    @staticmethod
    def Run(command, inputData):
        process = subprocess.Popen(command, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE,text=True)
        stdout = process.communicate(input=inputData)
        return stdout[0]

    def test_e2e_22_BoolTime(self):
        input = "2\n2\nGetDataForUser.csv\n04-10-2023 18:56\n8c417d9d-b13f-f070-bf07-1fd9c768126f\n"
        output = self.Run(["python", "../Functions/main.py"], input)
        lines = output.split('\n')
        print(output)
        self.assertEqual(lines[len(lines)-2], "{'wasUserOnline': False, 'nearestOnlineTime': '04-10-2023 18:59'}")