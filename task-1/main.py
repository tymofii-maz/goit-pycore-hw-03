from datetime import datetime

def get_days_from_today(date):
    try:
        input_date = datetime.strptime(date, "%Y-%m-%d").date()
    except (ValueError, TypeError):
        print(f"Неправильний формат дати: {date}. Потрібно 'РРРР-ММ-ДД'.")
        return None

    current_date = datetime.today().date()
    date_diff = current_date - input_date

    print(date_diff.days)

get_days_from_today("2022-02-24")
