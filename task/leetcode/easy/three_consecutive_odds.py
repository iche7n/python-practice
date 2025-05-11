"""
Дан целочисленный массив arr, вернуть, true если в массиве есть три последовательных нечетных числа.
В противном случае вернуть false.
"""

def threeConsecutiveOdds(arr: list[int]) -> bool:
    """
    Проверяет, содержит ли массив три последовательных нечётных числа.

    Возвращает:
        True — если найдены три подряд идущих нечётных числа.
        False — в противном случае.
    """
    arr_max = len(arr)

    for i in range(len(arr)):
        if i + 2 >= arr_max:
            break

        arr1 = arr[i]
        arr2 = arr[i + 1]
        arr3 = arr[i + 2]

        if arr1 % 2 != 0 and arr2 % 2 != 0 and arr3 % 2 != 0:
            return True

    return False


if __name__ == "__main__":
    arr = [1, 2, 34, 3, 4, 5, 7, 23, 12]
    print(threeConsecutiveOdds(arr))
