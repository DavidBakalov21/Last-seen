
import pandas as pd
import warnings
from datetime import datetime

warnings.simplefilter(action='ignore', category=Warning)
def PredictDataFor():
    date = input("Date:")
    ID = input("Id:")

    parsed_date = datetime.strptime(date, '%d-%m-%Y %H:%M')
    day_of_week = parsed_date.strftime('%A')
    time_of_day = parsed_date.strftime('%H:%M')
    DataFrame = pd.read_csv('/UserPredictTest.csv')
    UserData = DataFrame[DataFrame['ID'] == ID]
    UserData['Time'] = pd.to_datetime(UserData['Date'], format='%d-%m-%Y %H:%M').dt.strftime('%H:%M')
    was_online = UserData[(UserData['Day'] == day_of_week) & (UserData['Time']==time_of_day)].shape[0]
    print(was_online)
    UserData['Year-Week'] = pd.to_datetime(UserData['Date'], format='%d-%m-%Y %H:%M').dt.strftime('%Y-%U')
    total_weeks = UserData['Year-Week'].nunique()
    print(total_weeks)
    if total_weeks != 0:
        chance = was_online / total_weeks
    else:
        return "not enough data"
    return chance
print(PredictDataFor())