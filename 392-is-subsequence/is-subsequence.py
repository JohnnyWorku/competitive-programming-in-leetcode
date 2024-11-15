class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) > 0 and len(t) == 0:
            return False
        i = 0
        j = 0
        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                i += 1
                j += 1
            elif s[i] != t[j]:
                j += 1
        if i == j == 0:
            return True
        if (j == len(t) and i < len(s)) or (j == len(t) and i == len(s) and s[i - 1] != t[j - 1]):
            return False

        return True