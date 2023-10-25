import math

import pandas as pd
import warnings
from datetime import datetime

warnings.simplefilter(action='ignore', category=Warning)
def PredictData(file,date):
    parsed_date = datetime.strptime(date, '%d-%m-%Y %H:%M')
    formatted_date = parsed_date.strftime('%d-%m-%Y %H:%M')
    day_of_week = parsed_date.strftime('%A')
    DataFrame=pd.read_csv(file)
    CheckData=(DataFrame[DataFrame['Date']==formatted_date]).shape[0]

    if CheckData==0:
        DayData =DataFrame[DataFrame['Day'] == day_of_week]
        DayData['Time'] = pd.to_datetime(DayData['Date'], format='%d-%m-%Y %H:%M').dt.strftime('%H:%M')
        TimeFormatedData=DayData[DayData['Time'] == parsed_date.strftime('%H:%M')]
        grouped = TimeFormatedData.groupby('Date')
        groups = grouped.ngroups
        people = TimeFormatedData['Date'].shape[0]
        if groups!=0:
            return math.ceil(people/groups)
        else:
            return "bad data"
    else:
        return "this date already known"
#print(PredictDataFor())