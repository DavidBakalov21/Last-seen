import pandas as pd
import warnings

def DailyWeekly(file, ID):
    warnings.simplefilter(action='ignore', category=Warning)
    dataSet = pd.read_csv(file)
    userData = dataSet[dataSet['ID'] == ID]
    if userData.shape[0] != 0:
        userData['LastSeen'] = pd.to_datetime(userData['LastSeen'])
        userData['Week'] = pd.to_datetime(userData['Date'], format='%d-%m-%Y %H:%M').dt.isocalendar().week
        userData['Date'] = pd.to_datetime(userData['Date'], format='%d-%m-%Y %H:%M').dt.date
        dailyTotals = []
        for day_data in userData.groupby('Date'):
            start_time = None
            totalDuration = pd.Timedelta(0)
            for row in day_data[1].iterrows():
                if row[1]['isOnline'] and start_time is None:
                    start_time = row[1]['LastSeen']
                elif not row[1]['isOnline'] and start_time is not None:
                    end_time = row[1]['LastSeen']
                    totalDuration += (end_time - start_time)
                    start_time = None
            dailyTotals.append(totalDuration)
        weekly_totals_dict = {}
        for weekData in userData.groupby('Week'):
            start_time = None
            totalForWeek = pd.Timedelta(0)
            for row in weekData[1].iterrows():
                if row[1]['isOnline'] and start_time is None:
                    start_time = row[1]['LastSeen']
                elif not row[1]['isOnline'] and start_time is not None:
                    end_time = row[1]['LastSeen']
                    totalForWeek += (end_time - start_time)
                    start_time = None
            weekly_totals_dict[weekData[0]] = totalForWeek
        aDaily = sum(dailyTotals, pd.Timedelta(0)) / len(dailyTotals)
        aWeekly = sum(weekly_totals_dict.values(), pd.Timedelta(0)) / len(weekly_totals_dict)

        return {"weeklyAverage": aWeekly.total_seconds(), "dailyAverage": aDaily.total_seconds()}

    return "bad ID"


def Daily(file, ID):
    warnings.simplefilter(action='ignore', category=Warning)
    dataSet = pd.read_csv(file)
    userData = dataSet[dataSet['ID'] == ID]
    if userData.shape[0] != 0:
        userData['LastSeen'] = pd.to_datetime(userData['LastSeen'])
        userData['Date'] = pd.to_datetime(userData['Date'], format='%d-%m-%Y %H:%M').dt.date
        dailyTotals = []
        for day_data in userData.groupby('Date'):
            start_time = None
            totalDuration = pd.Timedelta(0)
            for row in day_data[1].iterrows():
                if row[1]['isOnline'] and start_time is None:
                    start_time = row[1]['LastSeen']
                elif not row[1]['isOnline'] and start_time is not None:
                    end_time = row[1]['LastSeen']
                    totalDuration += (end_time - start_time)
                    start_time = None
            dailyTotals.append(totalDuration)
        aDaily = sum(dailyTotals, pd.Timedelta(0)) / len(dailyTotals)
        return {"dailyAverage": aDaily.total_seconds()}
    else: return 'bad ID'


def Weekly(file, ID):
    warnings.simplefilter(action='ignore', category=Warning)
    dataSet = pd.read_csv(file)
    userData = dataSet[dataSet['ID'] == ID]
    if userData.shape[0] != 0:
        userData['LastSeen'] = pd.to_datetime(userData['LastSeen'])
        userData['Week'] = pd.to_datetime(userData['Date'], format='%d-%m-%Y %H:%M').dt.isocalendar().week
        weekly_totals_dict = {}
        for weekData in userData.groupby('Week'):
            start_time = None
            totalForWeek = pd.Timedelta(0)
            for row in weekData[1].iterrows():
                if row[1]['isOnline'] and start_time is None:
                    start_time = row[1]['LastSeen']
                elif not row[1]['isOnline'] and start_time is not None:
                    end_time = row[1]['LastSeen']
                    totalForWeek += (end_time - start_time)
                    start_time = None
            weekly_totals_dict[weekData[0]] = totalForWeek
        aWeekly = sum(weekly_totals_dict.values(), pd.Timedelta(0)) / len(weekly_totals_dict)
        return {"WeeklyAverage": aWeekly.total_seconds()}
    else: return 'bad ID'


#print(Daily('DailyWeekly.csv', '2fba2529-c166-8574-2da2-eac544d82634'))
#print(Weekly('DailyWeekly.csv', '2fba2529-c166-8574-2da2-eac544d82634'))
#print(DailyWeekly('DailyWeekly.csv', '2fba2529-c166-8574-2da2-eac544d82634'))
