import os

from Functions import FormatData
from Functions import ConvertToReadable
from Functions import OffsetLoop
from Functions import GetHistoricalData
from Functions import GetHDataForUser
from Functions import PredictHistData
from Functions import PredictForUser
from Functions import DateInput
from Functions import inputId
from Functions import DeleteUser
from Functions import TotalTime
from Functions import DailyWeekly
import requests
from Functions import MinMax
from Functions import TotalTimeOnRange
from Functions import CreateSaveReport
from Functions import Input
from Functions import GlobalDataReport
def main():
    WhatToDo=input("1-Offset Data, 2-Analyzing Data, 3-Delete and Prevent Data collection\n")

    if WhatToDo=="2":
        choice=input("1-GetHistoricalData, 2-GetDataForCertainUser, 3-PredictHIstoricalData, 4-PredictDataForuser, 5-Total time for user, 6-Daily Weekly, 7-TotalOnRange, 8-Min, 9-Max, 10-MakeReport, 11-SearchReport, 12-TotalReport\n")
        dataset=input("InputDataSet:\n")
        if choice=="1":
            date=DateInput.DateInput()
            print(GetHistoricalData.GetData(dataset, date))
            return GetHistoricalData.GetData(dataset, date)
        elif choice=="2":
            date=DateInput.DateInput()
            ID = inputId.IdInput()
            print(GetHDataForUser.GetDataForUser(dataset,date,ID))
            return GetHDataForUser.GetDataForUser(dataset,date,ID)
        elif choice=="3":
            date=DateInput.DateInput()
            print(PredictHistData.PredictData(dataset,date))
            return PredictHistData.PredictData(dataset,date)
        elif choice=="4":
            date=DateInput.DateInput()
            ID = inputId.IdInput()
            tolerance = float(input("tolerance:\n"))
            print(PredictForUser.PredictDataForUser(dataset,date,ID,tolerance))
            return PredictForUser.PredictDataForUser(dataset,date,ID,tolerance)
        elif choice=='5':
            ID = inputId.IdInput()
            print(TotalTime.TotalTime(dataset,ID))
            return TotalTime.TotalTime(dataset,ID)
        elif choice=='6':
            ID = inputId.IdInput()
            print(DailyWeekly.DailyWeekly(dataset, ID))
            return DailyWeekly.DailyWeekly(dataset, ID)

        elif choice=='7':
            Startdate = DateInput.DateInput()
            EndDate = DateInput.DateInput()
            ID = inputId.IdInput()
            print(TotalTimeOnRange.TotalTimeRange(dataset, ID,Startdate,EndDate))
            return TotalTimeOnRange.TotalTimeRange(dataset, ID,Startdate,EndDate)
        elif choice=='8':
            ID = inputId.IdInput()
            print(MinMax.Min(dataset, ID))
            return MinMax.Min(dataset, ID)
        elif choice=='9':
            ID = inputId.IdInput()
            print(MinMax.Max(dataset, ID))
            return MinMax.Max(dataset, ID)
        elif choice=='10':
            metrics=Input.INput("metrics")
            Users=Input.INput("users")
            res=CreateSaveReport.CreateRep(metrics,Users,dataset)
            print(res)
            DIR = os.path.dirname(os.path.abspath(__file__))
            file = os.path.join(DIR, 'DataBase')
            CreateSaveReport.Save(res,file)
            return res
        elif choice=='11':
            DIR = os.path.dirname(os.path.abspath(__file__))
            file = os.path.join(DIR, 'DataBase')
            name=Input.INput('Input report name')
            res=CreateSaveReport.SearchReport(name,file)
            print(res)
            return res
        elif choice=='12':
            startData=GlobalDataReport.ReadReportAndWriteData(dataset)
            res=GlobalDataReport.CalculateAv(startData)
            print(res)
            return res



    elif WhatToDo=="1":
        language=input("1-English, 2-Ukrainian\n")
        UserList= OffsetLoop.OffsetLoop()
        FormatedList={}

        for i in UserList:
            #FileWriter.ReadDataWriteData(i)
            FormatedList[i['nickname']]= FormatData.FormatData(i)
        finalList=[]
        for i in FormatedList:
            print(ConvertToReadable.ConvertToReadable({i:FormatedList[i]}, language))
            finalList.append(ConvertToReadable.ConvertToReadable({i:FormatedList[i]}, language))

        return finalList

    elif WhatToDo=="3":
        dataset = input("InputDataSet:\n")
        ID = inputId.IdInput()
        print(DeleteUser.DeleteData(dataset,ID))
        return DeleteUser.DeleteData(dataset,ID)

if __name__ == "__main__":
    main()


