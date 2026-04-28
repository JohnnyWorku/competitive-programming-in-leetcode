class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        digit_letter = {
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"]
        }

        res = []

        if len(digits) == 1:
            res = digit_letter[digits[0]]

        elif len(digits) == 2:
            for letter_1 in digit_letter[digits[0]]:
                for letter_2 in digit_letter[digits[1]]:
                    res.append(letter_1 + letter_2)

        elif len(digits) == 3:
            for letter_1 in digit_letter[digits[0]]:
                for letter_2 in digit_letter[digits[1]]:
                    for letter_3 in digit_letter[digits[2]]:
                        res.append(letter_1 + letter_2 + letter_3)

        elif len(digits) == 4:
            for letter_1 in digit_letter[digits[0]]:
                for letter_2 in digit_letter[digits[1]]:
                    for letter_3 in digit_letter[digits[2]]:
                        for letter_4 in digit_letter[digits[3]]:
                            res.append(letter_1 + letter_2 + letter_3 + letter_4)


        return res
        