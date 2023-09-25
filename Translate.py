def Translate(choice):
    language = {
        "1": ["User ", " was last seen at ", " (just now)", " (less than a minute ago)", " (couple of minutes ago)",
              " (hour ago)", " (today)", " (yesterday)", " (this week)", " (Long ago)", " is online"],

        "2": ["Користувач ", " в останнє був присутній ", " (тільки що)", " (менше хвилини тому)",
              " (декілька хвилин тому)",
              " (годину тому)", " (сьогодні)", " (вчора)", " (цього тижня)", " (давно)", " онлайн"]

    }
    return language[choice]
