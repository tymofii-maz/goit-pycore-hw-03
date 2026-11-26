import random

def get_numbers_ticket(min: int, max: int, quantity: int):
    if min < 1 or max > 1000 or min >= max:
        return []
    if quantity < 1 or quantity > (max - min + 1):
        return []

    results = set()

    while len(results) < quantity:
        number = random.randint(min, max)
        results.add(number)
    return sorted(results)

lottery_number = get_numbers_ticket(1, 49, 6)
print("Ваші лотерейні числа:", lottery_number)
