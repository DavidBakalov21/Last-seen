import pandas as pd
import warnings
warnings.simplefilter(action='ignore', category=Warning)
def NearestTime(ID,date,file):
    DataFrame = pd.read_csv(file)
    DataFrame['Date'] = pd.to_datetime(DataFrame['Date'], format='%d-%m-%Y %H:%M')
    User = DataFrame[DataFrame['ID'] == ID]
    date_provided = pd.to_datetime(date, format='%d-%m-%Y %H:%M')
    User['TimeDifference'] = (User['Date'] - date_provided).abs()
    nearest_entry = User[User['TimeDifference'] == User['TimeDifference'].min()]
    return nearest_entry['Date'].dt.strftime('%d-%m-%Y %H:%M').values[0]


def GetDataForUser(file,date,ID):

    DataFrame=pd.read_csv(file)
    User =DataFrame[DataFrame['ID'] == ID]
    if User.size!=0:
        FilterdUser=User[User['Date'] == date]
        if FilterdUser.size!=0:
            return {"wasUserOnline": True,"nearestOnlineTime": None}


        else:
            return {"wasUserOnline":False,"nearestOnlineTime": NearestTime(ID,date,file)}
    else:
        return {"wasUserOnline":False,"nearestOnlineTime": None}


#print(GetDataForUser())
