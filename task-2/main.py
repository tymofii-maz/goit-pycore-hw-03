import random

def get_numbers_ticket(min: int, max: int, quantity: int) -> list[int]:
    """
    Повертає відсортований список унікальних випадкових чисел для лотереї.

    min      - найменше можливе число (не менше 1)
    max      - найбільше можливе число (не більше 1000)
    quantity - скільки чисел потрібно вибрати

    Якщо параметри неправильні, повертає порожній список.
    """
    if min < 1 or max > 1000 or min >= max:
        return []
    if quantity < 1 or quantity > (max - min + 1):
        return []
        
    numbers = random.sample(range(min, max + 1), quantity)
    return sorted(numbers)

if __name__ == "__main__":
    lottery_number = get_numbers_ticket(1, 49, 6)
    print("Ваші лотерейні числа:", lottery_number)
