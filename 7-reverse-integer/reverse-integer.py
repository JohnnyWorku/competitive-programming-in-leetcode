class Solution:
    def reverse(self, x: int) -> int:
        reversed_x = 0
        number = x
        absolute_x = abs(x)
       
        while absolute_x > 0:
            num = absolute_x % 10
            reversed_x = reversed_x * 10 + num
            absolute_x //= 10

        if number < 0:
            reversed_x = -reversed_x

        if -2**31 <= reversed_x <= 2**31 - 1:
            return reversed_x
        
        return 0
