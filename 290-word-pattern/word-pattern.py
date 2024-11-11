class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        letter_word_dict = {}
        s = s.split(" ")
        j = 0

        if len(pattern) != len(s):
            return False

        for i in pattern:
            while j < len(s):
                if (i in letter_word_dict and letter_word_dict[i] != s[j]) or (i not in letter_word_dict and s[j] in letter_word_dict.values()):
                    return False
                else:
                    letter_word_dict[i] = s[j]
                    j += 1
                    break

        return True