class Solution:
    def isHappy(self, n: int) -> bool:
        product = 0

        if n < 10 and n == 1:
            return True
        elif n == 7:
            return True
        elif n < 10 and n != 1:
            return False

        while n > 0:
            num = n % 10
            product += num ** 2
            n //= 10

        return self.isHappy(product) 
