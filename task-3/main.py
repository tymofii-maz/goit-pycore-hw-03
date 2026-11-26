import re

def normalize_phone(phone_number: str):
    number_cleaned = re.sub(r"\D", "", phone_number)
    if len(number_cleaned) < 5 or len(number_cleaned) > 15:
        return
    if number_cleaned.startswith("0"):
        number_cleaned = f"+38{number_cleaned}"
    else:
        number_cleaned = f"+{number_cleaned}"
    return number_cleaned

raw_numbers = [
    "067\\t123 4567",
    "(095) 234-5678\\n",
    "+380 44 123 4567",
    "380501234567",
    "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11   ",
]

sanitized_numbers = [normalize_phone(num) for num in raw_numbers]
print("Нормалізовані номери телефонів для SMS-розсилки:", sanitized_numbers)
