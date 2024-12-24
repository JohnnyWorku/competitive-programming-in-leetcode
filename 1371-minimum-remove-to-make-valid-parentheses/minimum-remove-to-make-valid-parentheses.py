class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        res = []
        count = 0

        for i in range(len(s)):
            if s[i] == "(":
                res.append(s[i])
                count += 1
            elif s[i] == ")" and count > 0:
                res.append(s[i])
                count -= 1
            elif s[i].isalpha():
                res.append(s[i])

        filtered = []  # This is created because there can be unclosed brackets in the array ...
        for c in res[::-1]:  # We reversed res because most of the time unclosed brackets at the last positions makes the string invalid
            if c == "(" and count > 0:
                count -= 1
            else:
                filtered.append(c)

        return "".join(filtered[::-1])