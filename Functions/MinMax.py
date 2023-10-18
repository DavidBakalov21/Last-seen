import pandas as pd
def Min(file,ID):
    dataSet=pd.read_csv(file)
    filteredData=dataSet[dataSet['ID']==ID]
    start_time = None
    Arrayduration = []
    if filteredData.shape[0]!=0:
        for row in filteredData.iterrows():
            if row[1]['isOnline'] and start_time is None:
                start_time = row[1]['LastSeen']
            elif not row[1]['isOnline'] and start_time is not None:
                end_time = row[1]['LastSeen']
                end_time=pd.to_datetime(end_time)
                start_time=pd.to_datetime(start_time)
                Arrayduration.append((end_time - start_time).total_seconds())
                start_time = None
        return {"min time":min(Arrayduration)}
    else:
        return "ID is wrong"


def Max(file,ID):
    dataSet=pd.read_csv(file)
    filteredData=dataSet[dataSet['ID']==ID]
    start_time = None
    Arrayduration = []
    if filteredData.shape[0]!=0:
        for row in filteredData.iterrows():
            if row[1]['isOnline'] and start_time is None:
                start_time = row[1]['LastSeen']
            elif not row[1]['isOnline'] and start_time is not None:
                end_time = row[1]['LastSeen']
                end_time=pd.to_datetime(end_time)
                start_time=pd.to_datetime(start_time)
                Arrayduration.append((end_time - start_time).total_seconds())
                start_time = None
        return {"max time":max(Arrayduration)}
    else:
        return "ID is wrong"

#print(Min('C:/Users/Давід/PycharmProjects/LastSeen/Tests/outputF1.csv', '2fba2529-c166-8574-2da2-eac544d82634'))