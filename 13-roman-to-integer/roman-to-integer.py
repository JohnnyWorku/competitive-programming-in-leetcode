class Solution:
    def romanToInt(self, s: str) -> int:
        roman_to_int_dict = {
            "I" : 1,
            "V" : 5,
            "X" : 10,
            "L" : 50,
            "C" : 100,
            "D" : 500,
            "M" : 1000,
        }

        int_number = 0
        for a, b in zip(s, s[1:]):
            if roman_to_int_dict[a] < roman_to_int_dict[b]:
                int_number -= roman_to_int_dict[a]

            else:
                int_number += roman_to_int_dict[a]

        int_number += roman_to_int_dict[s[-1]]  

        return int_number
