import csv
from datetime import datetime


def ReadDataWriteData(Data):
    with open("Functions/output.csv", "a", newline='') as file:
        writer = csv.writer(file)
        if Data['isOnline'] == True:
            username = Data['nickname']
            ID= Data['userId']
            today_date = datetime.now().strftime('%d-%m-%Y %H:%M')
            day_of_week = datetime.now().strftime('%A')
            writer.writerow([username, today_date,day_of_week,ID])