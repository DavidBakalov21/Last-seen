import csv

import pandas as pd


def DeleteData(file,id):
    DataFrame=pd.read_csv(file)

    newDataSet = DataFrame[DataFrame['ID']==id]
    newDataSetNUM=newDataSet.shape[0]

    if newDataSetNUM==0:
        return "user wasn't present or id was incorect"
    newDataSet=DataFrame[DataFrame['ID']!=id]
    newDataSet.to_csv(file, index=False)
    with open("../ForbidenUsers.csv", "a", newline='') as file:
        writer = csv.writer(file)
        writer.writerow([id])

    return 'it was done'


#print(DeleteData('C:/Users/Давід/PycharmProjects/LastSeen/IntegrationTests/GetDataTest','224d4c53-5a76-6dc4-b32e-f61234538e7fDk'))