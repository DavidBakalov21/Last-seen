

def ReadReportAndWriteData(filePath):
    collected = []
    with open(filePath, "r") as file:
        for line in file:
            line = line.strip()
            if line.startswith("[{"):
                for i in eval(line):
                    collected.append(i)
    return collected

def CalculateAv(collectedData):
    AverageDict={}
    CountDict={}
    RESDict={}
    for i in collectedData:
        for key, value in i.items():
            if key not in AverageDict:
                AverageDict[key]=value
                CountDict[key]=1
            else:
                AverageDict[key]+=value
                CountDict[key]+=1
    for i in AverageDict:
        RESDict[i] = AverageDict[i] / CountDict[i]
    return RESDict



#a=ReadReportAndWriteData('C:/Users/Давід/PycharmProjects/LastSeen/Functions/Report')
#print(a)
#print(CalculateAv([{'min time': 3600.0}, {'max time': 25200.0}, {'dailyAverage': 43200.0}, {'WeeklyAverage': 43200.0}, {'min time': 3600.0}, {'max time': 25200.0}, {'dailyAverage': 43200.0}, {'WeeklyAverage': 43200.0}, {'min time': 3600.0}, {'max time': 25200.0}, {'dailyAverage': 43200.0}, {'WeeklyAverage': 43200.0}, {'min time': 3600.0}, {'max time': 25200.0}, {'dailyAverage': 43200.0}, {'WeeklyAverage': 43200.0}]))
