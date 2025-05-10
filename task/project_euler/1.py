"""
Если выписать все натуральные числа меньше 10,
кратные 3 или 5, то получим 3, 5, 6 и 9. Сумма этих чисел равна 23.
Найдите сумму всех чисел меньше 1000, кратных 3 или 5.
"""

def find_sum_natural_number(number1: int, number2: int, number_max: int) -> int:
    """
    Функция перебирает число от 1 до number_max,
    которая возвращает сумму чисел кратких number1 и number1
    """
    total = 0

    for i in range(1, number_max):
        if i % number1 == 0 or i % number2 == 0:
            total += i

    return total

if __name__ == "__main__":
    print(find_sum_natural_number(3, 5, 1000))

