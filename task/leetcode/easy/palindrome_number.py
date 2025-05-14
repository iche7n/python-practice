
class Solution:
    def isPalindrome(self, x: int) -> bool:
        """
        Проверяет, является ли целое число палиндромом.
        Палиндром читается одинаково слева направо и справа налево.
        """
        str_x = str(x)
        return str_x == str_x[::-1]
