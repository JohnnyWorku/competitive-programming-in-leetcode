class Solution:
    def isPalindrome(self, x: int) -> bool:
        a = x
        z = 0
        if x < 0:
            return False
        else:
            while x > 0:
                y = x % 10
                z = z * 10 + y
                x = x // 10

            if a == z:
                return True
           

        
        
        