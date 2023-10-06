import FormatData
import ConvertToReadable
import OffsetLoop
import FileWriter
language=input("1-English, 2-Ukrainian ")
UserList= OffsetLoop.OffsetLoop()
FormatedList={}

for i in UserList:
    #FileWriter.ReadDataWriteData(i)
    FormatedList[i['nickname']]= FormatData.FormatData(i)

for i in FormatedList:

    print(ConvertToReadable.ConvertToReadable({i:FormatedList[i]}, language))



