import pandas as pd
def GetData():
    date=input("Date:")
    DataFrame=pd.read_csv('C:/Users/Давід/PycharmProjects/LastSeen/Text.csv')
    num = (DataFrame['Date'] == date).sum()
    if num==0:
        return None
    return {"usersOnline": num}


print(GetData())





