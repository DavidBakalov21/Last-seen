import FormatData
import ConvertToReadable
import OffsetLoop
import FileWriter
import GetHistoricalData
import GetHDataForUser
import PredictHistData
import PredictForUser
WhatToDo=input("1-Offset Data, 2-Analyzing Data")

if WhatToDo=="2":
    choice=input("1-GetHistoricalData, 2-GetDataForCertainUser, 3-PredictHIstoricalData, 4-PredictDataForuser")
    dataset=input("InputDataSet:")
    if choice=="1":
        date = input("Date:")
        print(GetHistoricalData.GetData(dataset, date))
    elif choice=="2":
        date = input("Date:")
        ID = input("Id:")
        print(GetHDataForUser.GetDataForUser(dataset,date,ID))
    elif choice=="3":
        date = input("Date:")
        print(PredictHistData.PredictData(dataset,date))
    elif choice=="4":
        date = input("Date:")
        ID = input("Id:")
        tolerance = int(input("tolerance:"))
        print(PredictForUser.PredictDataForUser(dataset,date,ID,tolerance))
elif WhatToDo=="1":
    language=input("1-English, 2-Ukrainian ")
    UserList= OffsetLoop.OffsetLoop()
    FormatedList={}

    for i in UserList:
        FileWriter.ReadDataWriteData(i)
        FormatedList[i['nickname']]= FormatData.FormatData(i)

    for i in FormatedList:

        print(ConvertToReadable.ConvertToReadable({i:FormatedList[i]}, language))



