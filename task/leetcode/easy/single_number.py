"""
Given a non-empty array of integers nums, every element appears twice except for one.
Find that single one. You must implement a solution with a linear runtime complexity and
use only constant extra space.
"""

def single_number(nums: list[int]) -> int:
    """
    Функция ищет в списке число без повторений и возвращает его в результат
    """
    for i, _ in enumerate(nums):
        count = 0
        for j, _ in enumerate(nums):
            if nums[i] == nums[j]:
                count += 1
                letter = nums[i]

        if count == 1:
            return nums[i]

if __name__ == "__main__":
    print(single_number([1]))