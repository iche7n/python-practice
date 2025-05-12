"""
Каждый следующий элемент ряда Фибоначчи получается при сложении двух предыдущих.
Начиная с 1 и 2, первые 10 элементов будут:
1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
Найдите сумму всех четных элементов ряда Фибоначчи,
которые не превышают четыре миллиона.
"""


def find_fibonacci_sum(num1: int, num2: int, num_max: int) -> int:
    """
    Вычисляет сумму всех чётных элементов ряда Фибоначчи,
    начиная с num1 и num2, которые не превышают num_max.
    """
    num_sum = 0

    for _ in range(num_max):
        if num_sum >= num_max:
            return num_sum

        if num1 % 2 == 0:
            num_sum += num1

        if num2 % 2 == 0:
            num_sum += num2

        num1 += num2
        num2 += num1

    return num_sum


if __name__ == "__main__":
    print(find_fibonacci_sum(1, 2, 4000000))
