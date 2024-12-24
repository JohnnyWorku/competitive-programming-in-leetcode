class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        brackets_to_be_removed = []
        new_s = ""

        for i in range(len(s)):
            if not brackets_to_be_removed and s[i] == ")":
                brackets_to_be_removed.append(i)
            elif brackets_to_be_removed and (s[brackets_to_be_removed[-1]] == ")" and s[i] == ")"):
                brackets_to_be_removed.append(i)
            elif s[i] == "(":
                brackets_to_be_removed.append(i)
            elif brackets_to_be_removed and (s[brackets_to_be_removed[-1]] == "(" and s[i] == ")"):
                brackets_to_be_removed.pop()

        for j in range(len(s)):
            if j not in brackets_to_be_removed:
                new_s += s[j]
            else:
                continue

        return new_s