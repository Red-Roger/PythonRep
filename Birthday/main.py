from datetime import date, datetime


def get_birthdays_per_week(users):
    users ={}
    return users


if __name__ == "__main__":
    users = [
        {"name": "Jan Koum", "birthday": datetime(1976, 1, 1).date()},
    ]

    result = get_birthdays_per_week(users)
    print(result)
    # Виводимо результат
    for day_name, names in result.items():
        print(f"{day_name}: {', '.join(names)}")

users = [{"name": "Bill Gates", "birthday": datetime(1955, 10, 28).date()},
         {"name": "John Smith", "birthday": datetime(1956, 5, 2).date()},
         {"name": "Steven Spilberg", "birthday": datetime(1954, 9, 11).date()},
         {"name": "Vasia Pupkin", "birthday": datetime(1966, 3, 3).date()}]
