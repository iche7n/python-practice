"""
Имеется целочисленный массив nums и целочисленное число val,
удалите все вхождения val в num.
- Порядок элементов может быть изменен.
- После чего верните количество элементов в числах, которые не равны val
"""


def remove_element(nums: list[int], val: int) -> int:
    """
    Функция удаляет элементы из списка nums, которые равные val,
    после чего возвращают количество оставшихся элементов в списке
    """

    count = 0

    for i in range(len(nums)):
        if nums[i] != val:
            nums[count] = nums[i]
            count += 1
    return count


if __name__ == "__main__":
    print(remove_element([0,1,2,2,3,0,4,2], 2))