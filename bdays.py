from collections import defaultdict
from datetime import datetime, timedelta, date


def get_birthdays_per_week(users: list[dict]):
    bday_dict = defaultdict(list)
    for user in users:
        name = user["name"]
        bday = user["birthday"]
        bday_dict[(bday.month, bday.day)].append(name)

    weekend_names = []
    for day in [date.today() + timedelta(days=i) for i in range(7)]:
        if day.weekday() in [5, 6]:
            weekend_names.extend(bday_dict[(day.month, day.day)])
            continue
        
        names = bday_dict[(day.month, day.day)]
        if day.weekday() == 0:
            names.extend(weekend_names)

        if len(names) == 0:
            continue
        
        print(f"{day.strftime('%A')}: {', '.join(names)}")


users = [
    {"name": "Bill A", "birthday": datetime(1955, 2, 28)},
    {"name": "Alisa", "birthday": datetime(1985, 2, 27)},
    {"name": "Bob", "birthday": datetime(1955, 2, 25)},
]

get_birthdays_per_week(users)