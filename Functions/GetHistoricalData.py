import pandas as pd
def GetData(file,date):
    DataFrame=pd.read_csv(file)
    num = (DataFrame['Date'] == date).sum()
    if num==0:
        return None
    return {"usersOnline": num}


#print(GetData('C:/Users/Давід/PycharmProjects/LastSeen/Tests/GetDataTest', '04-10-2023 18:45'))





