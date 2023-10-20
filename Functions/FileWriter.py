import csv
from datetime import datetime, timezone


#def ReadDataWriteData(Data,file):
#    with open(file, "a", newline='') as file:
#        writer = csv.writer(file)
#        #if Data['isOnline'] == True:
#        username = Data['nickname']
#        ID= Data['userId']
#        isOnline=Data["isOnline"]
#        lastSeen=Data['lastSeenDate']
#        if lastSeen==None:
#            current_datetime = datetime.now(timezone.utc)
#            formatted_datetime = current_datetime.isoformat()
#            lastSeen=formatted_datetime
#        today_date = datetime.now().strftime('%d-%m-%Y %H:%M')
#        day_of_week = datetime.now().strftime('%A')
#        writer.writerow([username, today_date,day_of_week,ID,isOnline,lastSeen])