class Solution:
    def isPalindrome(self, x: int) -> bool:
        original_no = x
        last_digit = 0
        reversed_no = 0

        while x > 0:
            last_digit = x % 10
            reversed_no = reversed_no * 10 + last_digit
            x //= 10

        return reversed_no == original_no