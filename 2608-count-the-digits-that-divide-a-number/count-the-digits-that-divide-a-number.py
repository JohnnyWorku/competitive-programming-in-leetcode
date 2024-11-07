class Solution:
    def countDigits(self, num: int) -> int:
        num_copy = num
        counter = 0
        while num > 0:
            n = num % 10
            if num_copy % n == 0:
                counter += 1
            num //= 10

        return counter
