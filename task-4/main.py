from datetime import datetime, timedelta


def get_upcoming_birthdays(users: list[dict]) -> list[dict]:
    """
    Повертає список колег, яких треба привітати протягом 7 днів:
    від сьогодні до сьогодні + 6 днів включно.

    Якщо день народження випадає на суботу чи неділю,
    привітання переноситься на понеділок.
    Якщо сьогодні понеділок, вітаємо також тих,
    у кого день народження був у минулі вихідні.
    """
    MONDAY = 0
    SATURDAY = 5
    SUNDAY = 6
    DAYS_IN_PERIOD = 7  # сьогодні + 6 наступних днів

    def birthday_in_year(birthday, year):
        """Повертає день народження в потрібному році."""
        try:
            return birthday.replace(year=year)
        except ValueError:
            # Народився 29 лютого, а рік не високосний - святкуємо 28 лютого
            return birthday.replace(year=year, day=28)

    today = datetime.today().date()
    
    # Перший день періоду. У понеділок захоплюємо ще минулі суботу й неділю.
    start = today
    if today.weekday() == MONDAY:
        start = today - timedelta(days=2)

    # Останній день періоду
    end = today + timedelta(days=DAYS_IN_PERIOD - 1)
    result = []

    for user in users:
        birthday = datetime.strptime(user["birthday"], "%Y.%m.%d").date()
        # Найближчий день народження, не раніше початку періоду
        birthday_this_year = birthday_in_year(birthday, start.year)
        if birthday_this_year < start:
            birthday_this_year = birthday_in_year(birthday, start.year + 1)

        # Пропускаємо, якщо день народження після кінця періоду
        if birthday_this_year > end:
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

if __name__ == "__main__":
    users = [
        {"name": "John Doe", "birthday": "1985.01.23"},
        {"name": "Jane Smith", "birthday": "1990.01.27"},
        {"name": "Jason Smith", "birthday": "1995.11.27"},
        {"name": "Jason Smith", "birthday": "1998.02.28"},
        {"name": "Jack Smith", "birthday": "1999.12.02"},
    ]
    
    upcoming_birthdays = get_upcoming_birthdays(users)
    print("Список привітань на цьому тижні:", upcoming_birthdays)
