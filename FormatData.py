from datetime import timezone, datetime
def FormatData(data):
    if data['isOnline']==False:
        LSeen = datetime.fromisoformat(data['lastSeenDate'])
        currentTime = datetime.now().astimezone(timezone.utc)
        Differenc=currentTime-LSeen

        return Differenc
    else:
        return data['isOnline']