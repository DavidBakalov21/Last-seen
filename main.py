import requests
from datetime import datetime, timezone
def fetch_json(url):
    response = requests.get(url)
    response.raise_for_status()
    json_data = response.json()
    return json_data

def ConvertToReadable(info, user, language):
    if info!=True:
        if info.days<1 and info.seconds<30:
            if language=="1":
                return "User " + user + " was last seen at " + str(info)+" (just now)"
            else:
                return "Користувач " + user + " в останнє був присутній " + str(info) + " (тільки що)"

        elif info.days<1 and info.seconds < 60 and info.seconds>1:
            if language == "1":
                return "User " + user + " was last seen at " + str(info) + " (less than a minute ago)" #Ok
            else:
                return "Користувач " + user + " в останнє був присутній " + str(info) + " (менше хвилини тому)"

        elif info.days<1 and info.seconds < 3540 and info.seconds>60:
            if language == "1":
                return "User " + user + " was last seen at " + str(info) + " (couple of minutes ago)" #Ok
            else:
                return "Користувач " + user + " в останнє був присутній " + str(info) + " (декілька хвилин тому)"  # Ok

        elif info.days<1 and info.seconds < 7140 and info.seconds>3600:
            if language == "1":
                return "User " + user + " was last seen at " + str(info) + " (hour ago)" #Ok
            else:
                return "Користувач " + user + " в останнє був присутній " + str(info) + " (годину тому)" # Ok

        elif info.seconds>7200 and info.days<1:
            if language == "1":
                return "User " + user + " was last seen at " + str(info) + " (today)" #Ok
            else:
                return "Користувач " + user + " в останнє був присутній " + str(info) + " (сьогодні)" # Ok

        elif info.days==1:
            if language == "1":
                return "User " + user + " was last seen at " + str(info) + " (yesterday)" #Ok
            else:
                return "Користувач " + user + " в останнє був присутній " + str(info) + " (вчора)" # Ok

        elif info.days>1 and info.days<7:
            if language == "1":
                return "User " + user + " was last seen at " + str(info) + " (this week)" #OK
            else:
                return "Користувач " + user + " в останнє був присутній " + str(info) + " (цього тижня)" # Ok

        else:
            if language == "1":
                return "User " + user + " was last seen at " + str(info) + " (Long ago)" #OK
            else:
                return "Користувач " + user + " в останнє був присутній " + str(info) + " (давно)" # Ok
    else:
        if language == "1":
            return "User " + user + " is online" #Ok
        else:
            return "Користувач " + user + " онлайн"  # Ok
language=input("1-English, 2-Ukrainian ")
UserList=[]
offset=0
starter=0
while True:
    url = "https://sef.podkolzin.consulting/api/users/lastSeen?offset="+str(offset)
    data = fetch_json(url)
    if (starter==0 and  len(data["data"])>0) or  len(data["data"])>0 :
        UserList.extend(data["data"])
    else:
        print("Failed to fetch data.")
        break
    offset+=len(data["data"])
    starter+=1
 #   print(data)

FormatedList={}
for i in UserList:
    #if i['lastSeenDate']!=None:
    if i['isOnline']==False:
        LSeen = datetime.fromisoformat(i['lastSeenDate'])
        currentTime = datetime.now().astimezone(timezone.utc)
        Differenc=currentTime-LSeen
        FormatedList[i['nickname']]=Differenc
    else:
        FormatedList[i['nickname']] = i['isOnline']

#print(FormatedList)


for i in FormatedList:
    print(ConvertToReadable(FormatedList[i], i, language))