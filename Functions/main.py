import FormatData
import ConvertToReadable
import OffsetLoop
import FileWriter
import GetHistoricalData
import GetHDataForUser
import PredictHistData
import PredictForUser
import DateInput
import inputId
import DeleteUser
import TotalTime
import DailyWeekly
import requests
WhatToDo=input("1-Offset Data, 2-Analyzing Data, 3-Delete and Prevent Data collection\n")

if WhatToDo=="2":
    choice=input("1-GetHistoricalData, 2-GetDataForCertainUser, 3-PredictHIstoricalData, 4-PredictDataForuser, 5-Total time for user, 6-Daily Weekly\n")
    dataset=input("InputDataSet:\n")
    if choice=="1":
        date=DateInput.DateInput()
        print(GetHistoricalData.GetData(dataset, date))
    elif choice=="2":
        date=DateInput.DateInput()
        ID = inputId.IdInput()
        print(GetHDataForUser.GetDataForUser(dataset,date,ID))
    elif choice=="3":
        date=DateInput.DateInput()
        print(PredictHistData.PredictData(dataset,date))
    elif choice=="4":
        date=DateInput.DateInput()
        ID = inputId.IdInput()
        tolerance = float(input("tolerance:\n"))
        print(PredictForUser.PredictDataForUser(dataset,date,ID,tolerance))
    elif choice=='5':
        ID = inputId.IdInput()
        print(TotalTime.TotalTime(dataset,ID))
    elif choice=='6':
        ID = inputId.IdInput()
        print(DailyWeekly.DailyWeekly(dataset, ID))


elif WhatToDo=="1":
    language=input("1-English, 2-Ukrainian\n")
    UserList= OffsetLoop.OffsetLoop()
    FormatedList={}

    for i in UserList:
        #FileWriter.ReadDataWriteData(i)
        FormatedList[i['nickname']]= FormatData.FormatData(i)

    for i in FormatedList:

        print(ConvertToReadable.ConvertToReadable({i:FormatedList[i]}, language))

elif WhatToDo=="3":
    dataset = input("InputDataSet:\n")
    ID = inputId.IdInput()
    print(DeleteUser.DeleteData(dataset,ID))

