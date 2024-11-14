class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        s = list(s)
        index = 0
        for i in t:
            if i in s:
                s.pop(s.index(i))
            elif i not in s[index + 1:]: 
                return i
