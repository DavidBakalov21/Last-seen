import math

import pandas as pd
import warnings
from datetime import datetime

warnings.simplefilter(action='ignore', category=Warning)
def PredictDataFor():
    date=input("Date:")
    parsed_date = datetime.strptime(date, '%d-%m-%Y %H:%M')
    day_of_week = parsed_date.strftime('%A')
    DataFrame=pd.read_csv('C:/Users/Давід/PycharmProjects/LastSeen/Text.csv')
    DayData =DataFrame[DataFrame['Day'] == day_of_week]
    DayData['Time'] = pd.to_datetime(DayData['Date'], format='%d-%m-%Y %H:%M').dt.strftime('%H:%M')
    TimeFormatedData=DayData[DayData['Time'] == parsed_date.strftime('%H:%M')]
    grouped = TimeFormatedData.groupby('Date')
    groups = grouped.ngroups
    people = len(TimeFormatedData['Date'])
    return math.ceil(people/groups)
print(PredictDataFor())