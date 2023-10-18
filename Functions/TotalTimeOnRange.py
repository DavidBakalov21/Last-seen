import pandas as pd
def TotalTimeRange(file,ID, startRange,endRange):

    dataSet=pd.read_csv(file)
    dataSet['LastSeen'] = pd.to_datetime(dataSet['LastSeen'], utc=True)
    filteredData=dataSet[dataSet['ID']==ID]
    start_time = None
    total_duration = pd.Timedelta(0)
    startRange = pd.to_datetime(startRange)
    endRange = pd.to_datetime(endRange)

    # Filter by date range
    filteredData = filteredData[(filteredData['LastSeen'] >= startRange) & (filteredData['LastSeen'] <= endRange)]
    if filteredData.shape[0]!=0:
        for row in filteredData.iterrows():
            if row[1]['isOnline'] and start_time is None:
                start_time = row[1]['LastSeen']
            elif not row[1]['isOnline'] and start_time is not None:
                end_time = row[1]['LastSeen']
                end_time=pd.to_datetime(end_time)
                start_time=pd.to_datetime(start_time)
                total_duration += (end_time - start_time)
                start_time = None
        return {"totalTime":total_duration.total_seconds()}
    else:
        return "ID is wrong"

#print(TotalTimeRange('C:/Users/Давід/PycharmProjects/LastSeen/Tests/outputRange.csv', '2fba2529-c166-8574-2da2-eac544d82634', '2023-10-10T17:25:41.988544+00:00', '2023-10-11T20:21:41.988544+00:00'))