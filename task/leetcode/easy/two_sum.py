"""
Дан массив целых чисел nums и целое число target,
вернуть индексы двух чисел, чтобы их сумма давала target.
Вы можете предположить, что каждый вход будет иметь ровно одно решение,
и вы не можете использовать один и тот же элемент дважды.
"""


def two_sum(nums: list[int], target: int) -> list[int]:
    """
    Возвращает индексы двух чисел из списка nums, сумма которых равна target.

    Предполагается, что существует ровно одно решение,
    и нельзя использовать один и тот же элемент дважды.
    """
    result = []

    for i, _ in enumerate(nums):
        for j, _ in enumerate(nums):
            if target == (nums[i] + nums[j]):
                if i != j:
                    result.append(i)
                    result.append(j)
                    return result


if __name__ == "__main__":
    nums = [2, 7, 11, 15]
    target = 9

    print(two_sum(nums, target))