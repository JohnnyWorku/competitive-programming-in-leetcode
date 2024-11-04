class Solution:
    def addDigits(self, num: int) -> int:
        sum_num = 0

        if num < 10:
            return num

        while num > 0:
            sum_num += (num % 10)
            num //= 10

        return self.addDigits(sum_num) 



        
