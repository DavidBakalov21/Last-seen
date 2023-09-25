import FormatData
import ConvertToReadable
import OffsetLoop
language=input("1-English, 2-Ukrainian ")
UserList=OffsetLoop.OffsetLoop()
FormatedList={}
for i in UserList:

    FormatedList[i['nickname']]=FormatData.FormatData(i)
for i in FormatedList:
    print(ConvertToReadable.ConvertToReadable({i:FormatedList[i]}, language))