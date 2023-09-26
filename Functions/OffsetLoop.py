
from Functions.fetch_json import fetch_json
def OffsetLoop():
    UserList = []
    offset = 0
    starter = 0
    while True:
        url = "https://sef.podkolzin.consulting/api/users/lastSeen?offset=" + str(offset)
        data = fetch_json(url)
        if (starter == 0 and len(data["data"]) > 0) or len(data["data"]) > 0:
            UserList.extend(data["data"])
        else:
           # print("Failed to fetch data.")
            break
        offset += len(data["data"])
        starter += 1
    return UserList