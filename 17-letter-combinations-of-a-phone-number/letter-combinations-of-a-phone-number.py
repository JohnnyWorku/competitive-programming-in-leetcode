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

        def backtrack(i, curr_str):
            if len(curr_str) == len(digits):
                res.append(curr_str)
                return

            for char in digit_letter[digits[i]]:
                backtrack(i + 1, curr_str + char)

        backtrack(0, "")

        return res
        