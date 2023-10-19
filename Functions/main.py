from . import FormatData
from . import ConvertToReadable
from . import OffsetLoop
from . import GetHistoricalData
from . import GetHDataForUser
from . import PredictHistData
from . import PredictForUser
from . import DateInput
from . import inputId
from . import DeleteUser
from . import TotalTime
from . import DailyWeekly
import requests
from . import MinMax
from . import TotalTimeOnRange
def main():
    WhatToDo=input("1-Offset Data, 2-Analyzing Data, 3-Delete and Prevent Data collection\n")

    if WhatToDo=="2":
        choice=input("1-GetHistoricalData, 2-GetDataForCertainUser, 3-PredictHIstoricalData, 4-PredictDataForuser, 5-Total time for user, 6-Daily Weekly, 7-TotalOnRange, 8-Min, 9-Max\n")
        dataset=input("InputDataSet:\n")
        if choice=="1":
            date=DateInput.DateInput()
            return GetHistoricalData.GetData(dataset, date)
        elif choice=="2":
            date=DateInput.DateInput()
            ID = inputId.IdInput()
            return GetHDataForUser.GetDataForUser(dataset,date,ID)
        elif choice=="3":
            date=DateInput.DateInput()
            return PredictHistData.PredictData(dataset,date)
        elif choice=="4":
            date=DateInput.DateInput()
            ID = inputId.IdInput()
            tolerance = float(input("tolerance:\n"))
            return PredictForUser.PredictDataForUser(dataset,date,ID,tolerance)
        elif choice=='5':
            ID = inputId.IdInput()
            return TotalTime.TotalTime(dataset,ID)
        elif choice=='6':
            ID = inputId.IdInput()
            return DailyWeekly.DailyWeekly(dataset, ID)

        elif choice=='7':
            Startdate = DateInput.DateInput()
            EndDate = DateInput.DateInput()
            ID = inputId.IdInput()
            return TotalTimeOnRange.TotalTimeRange(dataset, ID,Startdate,EndDate)
        elif choice=='8':
            ID = inputId.IdInput()
            return MinMax.Min(dataset, ID)
        elif choice=='9':
            ID = inputId.IdInput()
            return MinMax.Max(dataset, ID)


    elif WhatToDo=="1":
        language=input("1-English, 2-Ukrainian\n")
        UserList= OffsetLoop.OffsetLoop()
        FormatedList={}

        for i in UserList:
            #FileWriter.ReadDataWriteData(i)
            FormatedList[i['nickname']]= FormatData.FormatData(i)
        finalList=[]
        for i in FormatedList:

            finalList.append(ConvertToReadable.ConvertToReadable({i:FormatedList[i]}, language))

        return finalList

    elif WhatToDo=="3":
        dataset = input("InputDataSet:\n")
        ID = inputId.IdInput()
        return DeleteUser.DeleteData(dataset,ID)

if __name__ == "__main__":
    main()

