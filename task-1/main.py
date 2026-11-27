from datetime import datetime

def get_days_from_today(date: str) -> int | None:
    """
    Рахує, скільки днів минуло від заданої дати до сьогодні.

    date - рядок у форматі 'РРРР-ММ-ДД', наприклад '2020-10-09'.
    Якщо дата в майбутньому, результат буде від'ємним.
    Якщо формат неправильний, функція повертає None.
    """
    try:
        input_date = datetime.strptime(date, "%Y-%m-%d").date()
    except (ValueError, TypeError):
        print(f"Неправильний формат дати: {date}. Потрібно 'РРРР-ММ-ДД'.")
        return None

    current_date = datetime.today().date()
    date_diff = current_date - input_date

    return date_diff.days

if __name__ == "__main__":
    print(get_days_from_today("2022-02-24"))
