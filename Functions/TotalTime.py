import pandas as pd
def TotalTime(file,ID):
    dataSet=pd.read_csv(file)
    filteredData=dataSet[dataSet['ID']==ID]
    start_time = None
    total_duration = pd.Timedelta(0)
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

#print(TotalTime('C:/Users/Давід/PycharmProjects/LastSeen/Tests/outputF1.csv', '2fba2529-c166-8574-2da2-eac544d82634'))
#print(TotalTime('outputF1.csv', '2fba2529-c166-8574-2da2-eac544d8263Nfbdxc4'))






