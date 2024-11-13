class Solution:
    def firstUniqChar(self, s: str) -> int:
        letter_dict = {}

        for index, letter in enumerate(s):
            if letter in letter_dict:
                letter_dict[letter] -= index
            else:
                letter_dict[letter] = index

        for letters in letter_dict:
            if letter_dict[letters] >= 0:
                return letter_dict[letters]

        return -1