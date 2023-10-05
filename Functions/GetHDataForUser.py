import pandas as pd
import warnings
warnings.simplefilter(action='ignore', category=Warning)
def NearestTime(ID,date):
    DataFrame = pd.read_csv('C:/Users/Давід/PycharmProjects/LastSeen/Text.csv')
    DataFrame['Date'] = pd.to_datetime(DataFrame['Date'], format='%d-%m-%Y %H:%M')
    User = DataFrame[DataFrame['ID'] == ID]
    date_provided = pd.to_datetime(date, format='%d-%m-%Y %H:%M')
    User['TimeDifference'] = (User['Date'] - date_provided).abs()
    nearest_entry = User[User['TimeDifference'] == User['TimeDifference'].min()]
    return nearest_entry['Date'].dt.strftime('%d-%m-%Y %H:%M').values[0]


def GetDataForUser():
    date=input("Date:")
    ID=input("Id:")
    DataFrame=pd.read_csv('C:/Users/Давід/PycharmProjects/LastSeen/Text.csv')
    User =DataFrame[DataFrame['ID'] == ID]
    if User.size!=0:
        FilterdUser=User[User['Date'] == date]
        if FilterdUser.size!=0:
            return {"wasUserOnline": True,"nearestOnlineTime": None}


        else:
            return {"wasUserOnline":False,"nearestOnlineTime": NearestTime(ID,date)}
    else:
        return {"wasUserOnline":False,"nearestOnlineTime": None}


print(GetDataForUser())
