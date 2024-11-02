class Solution:
    def myAtoi(self, s: str) -> int:
        s_number = ""
        number = 0
        s = s.lstrip()
        counter = 0  # To count the number of characters it viewed

        if len(s) == 0 or s[0].isalpha():
            return 0

        for char in s:
            if (s[0] == char == "-" or s[0] == char == "+") and counter < 1:
                counter += 1
                continue
               
            if char.isdigit():
                s_number += char
            elif not char.isdigit():
                break

        for num in s_number:
            n = ord(num) - ord("0")
            number = number * 10 + n

        if s[0] == "-":
            if -number < -2 ** 31:
                return -2 ** 31
            
            return -number

        else:
            if number > 2 ** 31 - 1:
                return 2 ** 31 - 1

            return number

            