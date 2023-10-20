from Functions import MinMax
from Functions import DailyWeekly
from Functions import TotalTimeOnRange
def CreateRep(metricsList, userlist, dataset):
    if isinstance(metricsList, str):
        metricsList = metricsList.split(',')
    if isinstance(userlist, str):
        userlist = userlist.split(',')
    Report={}
    StartTime=None
    EndTime=None
    if 'total' in metricsList:
        StartTime=input('start time:')
        EndTime=input('End time:')
    for user in userlist:
        Report[user] = []
        for command in metricsList:
            if command=="min":
                Report[user].append(MinMax.Min(dataset,user))
            if command=='max':
                Report[user].append(MinMax.Max(dataset, user))
            if command=='daily':
                Report[user].append(DailyWeekly.Daily(dataset, user))
            if command=='weekly':
                Report[user].append(DailyWeekly.Weekly(dataset, user))
            if command=='total':
                Report[user].append(TotalTimeOnRange.TotalTimeRange(dataset, user,StartTime,EndTime))
    return Report

def Save(Report,saveFile):
    Name=input("Input report Name:")
    with open(saveFile, "a", newline='') as file:
        file.write(f"Report Name: {Name}\n")
        for data in Report.items():
            file.write(f"{data[0]}:\n")
            file.write(f"\t{data[1]}\n")
        file.write("\n")




def SearchReport(searchName, saveFile):
    with open(saveFile, "r") as file:
        reportFound = False
        collectedLines = []
        for line in file:
            if line.strip() == f"Report Name: {searchName}":
                reportFound = True
                collectedLines.append(line.strip())
            elif reportFound==True:
                if line == '\n':
                    break
                collectedLines.append(line.strip())
    if not reportFound:
        return "No report found with the name'."
    return collectedLines

#Report=CreateRep(['min', 'max', 'daily', 'weekly'], ['2fba2529-c166-8574-2da2-eac544d82634','2fba2529-c166-8574-2da2-eac544d826341'],'C:/Users/Давід/PycharmProjects/LastSeen/Functions/ReportTestDataSet')
#print(Report)
#Save(Report,'Report')

#print(SearchReport('Rep1', 'Report'))










