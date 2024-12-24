class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        new_s = ""
        l, r = 0, 0

        while l < len(s) and r < len(spaces):
            new_s += s[l: spaces[r]] + " " 
            l = spaces[r]
            r += 1

        if l < len(s):
            new_s += s[l:]

        return new_s
