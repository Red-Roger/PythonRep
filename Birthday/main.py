from datetime import date, datetime


def get_birthdays_per_week(users):
    
    WEEKNAMES = {0:"Monday", 1:"Tuesday", 2:"Wednesday", 3:"Thursday", 4:"Friday", 5:"Saturday", 6:"Sunday"}
    users_birth = {}
    today = date.today()
    
    if users == []:
        return users_birth

    for value in users:
        user_birth = value ["birthday"]

        if today.month == 12 and today.day > 24 and user_birth.month == 1:
            user_birth_norm = user_birth.replace (year = today.year + 1)
        else:
            user_birth_norm = user_birth.replace (year = today.year)
 
        difference = user_birth_norm - today

        if difference.days >= 0 and difference.days < 8:
            index = user_birth_norm.weekday()
            if index == 5 or index == 6:
                index = 0
            user_birth_name = WEEKNAMES[index]
            if users_birth.get(user_birth_name):
                users_birth [WEEKNAMES[index]].append (value["name"])
            else:
                users_birth [WEEKNAMES[index]] = [value["name"]]

    return users_birth


if __name__ == "__main__":
    users = [
        {"name": "Jan Koum", "birthday": datetime(1976, 11, 14).date()},
    ]

    result = get_birthdays_per_week(users)
    print(result)
    # Виводимо результат
    for day_name, names in result.items():
        print(f"{day_name}: {', '.join(names)}")

