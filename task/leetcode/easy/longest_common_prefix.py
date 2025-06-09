"""
Напишите функцию, которая найдет самую длинную строку с общим префиксом среди массива строк.

Если общего префикса нет, верните пустую строку.

Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.

Нам нужно проверить каждую букву в слове и при true - записывать ее в новую строку, пока буквы совпадают

Найти самую короткую строку в листе и показать ее + размер


strings = ["apple", "kiwi", "banana", "fig"]

# Предположим, что первая строка — самая короткая
shortest = strings[0]

# Проходим по остальным строкам
for s in strings[1:]:
    if len(s) < len(shortest):
        shortest = s

print("Самая короткая строка:", shortest)


"""


def func(word_list: list):
    shortest = word_list[0]
    min_len = 0

    # Определяем минимальный индекс
    for i in word_list[1:]:
        if len(i) < len(shortest):
            min_len = len(i)

    letter = word_list[0]

    for x in range(min_len):
        if letter[:x] == (word_list[1][:x] and word_list[2][:x]):
            print(letter[:x])




if __name__ == "__main__":
    func(["flower","flow","flight"])