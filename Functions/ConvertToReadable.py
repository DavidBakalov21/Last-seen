from Functions.Translate import Translate
#I want to commit
def ConvertToReadable(info, language):
    user=list(info.keys())[0]
    info=list(info.values())[0]
    TranslateArray= Translate(language)
    if info!=True:
        if info.days<1 and info.seconds<30:
            return TranslateArray[0] + user + TranslateArray[1] + str(info)+TranslateArray[2]
        elif info.days<1 and info.seconds < 60 and info.seconds>1:
            return TranslateArray[0] + user + TranslateArray[1] + str(info) + TranslateArray[3] #Ok
        elif info.days<1 and info.seconds < 3540 and info.seconds>60:
            return TranslateArray[0] + user + TranslateArray[1] + str(info) + TranslateArray[4] #Ok
        elif info.days<1 and info.seconds < 7140 and info.seconds>3600:
            return TranslateArray[0] + user + TranslateArray[1] + str(info) + TranslateArray[5] #Ok
        elif info.seconds>7200 and info.days<1:
            return TranslateArray[0] + user + TranslateArray[1] + str(info) + TranslateArray[6] #Ok
        elif info.days==1:
            return TranslateArray[0] + user + TranslateArray[1] + str(info) + TranslateArray[7] #Ok
        elif info.days>1 and info.days<7:
            return TranslateArray[0] + user + TranslateArray[1] + str(info) + TranslateArray[8] #OK
        else:
            return TranslateArray[0] + user + TranslateArray[1] + str(info) + TranslateArray[9] #OK
    else:
        return TranslateArray[0] + user + TranslateArray[10] #Ok




