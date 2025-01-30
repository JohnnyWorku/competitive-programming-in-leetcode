class Solution:
    def isPalindrome(self, x: int) -> bool:
        original_no = x
        reversed_no = 0

        while x > 0:
            last_digit = x % 10
            reversed_no = reversed_no * 10 + last_digit
            x //= 10

        return True if original_no == reversed_no else False
           

        
        
        