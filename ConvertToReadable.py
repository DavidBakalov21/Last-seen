def ConvertToReadable(info, user, language):
    if info!=True:
        if info.days<1 and info.seconds<30:
            if language=="1":
                return "User " + user + " was last seen at " + str(info)+" (just now)"
            else:
                return "Користувач " + user + " в останнє був присутній " + str(info) + " (тільки що)"

        elif info.days<1 and info.seconds < 60 and info.seconds>1:
            if language == "1":
                return "User " + user + " was last seen at " + str(info) + " (less than a minute ago)" #Ok
            else:
                return "Користувач " + user + " в останнє був присутній " + str(info) + " (менше хвилини тому)"

        elif info.days<1 and info.seconds < 3540 and info.seconds>60:
            if language == "1":
                return "User " + user + " was last seen at " + str(info) + " (couple of minutes ago)" #Ok
            else:
                return "Користувач " + user + " в останнє був присутній " + str(info) + " (декілька хвилин тому)"  # Ok

        elif info.days<1 and info.seconds < 7140 and info.seconds>3600:
            if language == "1":
                return "User " + user + " was last seen at " + str(info) + " (hour ago)" #Ok
            else:
                return "Користувач " + user + " в останнє був присутній " + str(info) + " (годину тому)" # Ok

        elif info.seconds>7200 and info.days<1:
            if language == "1":
                return "User " + user + " was last seen at " + str(info) + " (today)" #Ok
            else:
                return "Користувач " + user + " в останнє був присутній " + str(info) + " (сьогодні)" # Ok

        elif info.days==1:
            if language == "1":
                return "User " + user + " was last seen at " + str(info) + " (yesterday)" #Ok
            else:
                return "Користувач " + user + " в останнє був присутній " + str(info) + " (вчора)" # Ok

        elif info.days>1 and info.days<7:
            if language == "1":
                return "User " + user + " was last seen at " + str(info) + " (this week)" #OK
            else:
                return "Користувач " + user + " в останнє був присутній " + str(info) + " (цього тижня)" # Ok

        else:
            if language == "1":
                return "User " + user + " was last seen at " + str(info) + " (Long ago)" #OK
            else:
                return "Користувач " + user + " в останнє був присутній " + str(info) + " (давно)" # Ok
    else:
        if language == "1":
            return "User " + user + " is online" #Ok
        else:
            return "Користувач " + user + " онлайн"  # Ok
