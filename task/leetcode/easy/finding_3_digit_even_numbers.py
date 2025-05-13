"""
You are given an integer array digits, where each element is a digit. The array may contain duplicates.

You need to find all the unique integers that follow the given requirements:

The integer consists of the concatenation of three elements from digits in any arbitrary order.
The integer does not have leading zeros.
The integer is even.
For example, if the given digits were [1, 2, 3], integers 132 and 312 follow the requirements.

Return a sorted array of the unique integers.

Вам задан целочисленный массив digits, где каждый элемент представляет собой цифру. Массив может содержать дубликаты.

Вам нужно найти все уникальные целые числа, соответствующие заданным требованиям:

Целое число состоит из объединения трех элементов из цифр в любом произвольном порядке.
Целое число не содержит нулей в начале.
Целое число является четным.
Например, если заданы цифры [1, 2, 3], то целые числа 132 и 312 соответствуют требованиям.

Возвращает отсортированный массив уникальных целых чисел.


Пример 1:
Ввод: цифры = [2,1,3,0]
Вывод: [102,120,130,132,210,230,302,310,312,320]
Пояснение: Все возможные целые числа, соответствующие требованиям, содержатся в выходном массиве.
Обратите внимание, что в нем нет нечетных чисел или целых чисел с начальными нулями.

Пример 2:
Ввод: цифры = [2,2,8,8,2]
Выходные данные: [222,228,282,288,822,828,882]
Пояснение: Одна и та же цифра может использоваться столько раз, сколько она обозначена цифрами.
В этом примере цифра 8 используется дважды в числах 288, 828 и 882.

Пример 3:
Ввод: цифры = [3,7,5]
Вывод: []
Пояснение: Никакие четные целые числа не могут быть сформированы с использованием заданных цифр.

class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:


"""
from typing import List

class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        num_list = []

        for i, _ in enumerate(digits):
            for y, _ in enumerate(digits):
                for n, _ in enumerate(digits):
                    if i == y or y == n or n == i:
                        continue

                    numbers = int(f"{digits[i]}{digits[y]}{digits[n]}")
                    if numbers < 100:
                        continue

                    if numbers % 2 == 0:
                        num_list.append(numbers)

        num_list = list(set(num_list))
        num_list = sorted(num_list)
        return num_list

