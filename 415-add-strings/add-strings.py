class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        sys.set_int_max_str_digits(10**6)
        n1 = 0
        n2 = 0
        for i in num1:
            n1 = n1 * 10 + ord(i) - ord('0')
        for j in num2:
            n2 = n2 * 10 + ord(j) - ord('0')

        result = n1 + n2

        return f"{result}"