from datetime import datetime, timedelta


def get_upcoming_birthdays(users):

    SATURDAY = 5
    SUNDAY = 6

    def birthday_in_year(birthday, year):
    # Повертає день народження в потрібному році.
        try:
            return birthday.replace(year=year)
        except ValueError:
            # Народився 29 лютого, а рік не високосний - святкуємо 28 лютого
            return birthday.replace(year=year, day=28)

    today = datetime.today().date()
    result = []

    for user in users:
        birthday = datetime.strptime(user["birthday"], "%Y.%m.%d").date()

        birthday_this_year = birthday_in_year(birthday, today.year)

        if birthday_this_year < today:
            birthday_this_year = birthday_in_year(birthday, today.year + 1)

        days_left = (birthday_this_year - today).days

        if days_left > 7:
            continue

        congratulation_date = birthday_this_year

        if congratulation_date.weekday() == SATURDAY:
            congratulation_date = congratulation_date + timedelta(days=2)
        elif congratulation_date.weekday() == SUNDAY:
            congratulation_date = congratulation_date + timedelta(days=1)

        result.append({
            "name": user["name"],
            "congratulation_date": congratulation_date.strftime("%Y.%m.%d"),
        })

    return result

users = [
    {"name": "John Doe", "birthday": "1985.01.23"},
    {"name": "Jane Smith", "birthday": "1990.01.27"},
    {"name": "Jason Smith", "birthday": "1990.11.27"},
]

upcoming_birthdays = get_upcoming_birthdays(users)
print("Список привітань на цьому тижні:", upcoming_birthdays)
