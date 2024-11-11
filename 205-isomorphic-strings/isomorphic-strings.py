class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        letter_dict = {}

        j = 0
        for i in s:
            while j < len(t):
                if (i in letter_dict and letter_dict[i] != t[j]) or (i not in letter_dict and t[j] in letter_dict.values()):
                    return False
                else:
                    letter_dict[i] = t[j]
                    j += 1
                    break

        return True
