class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        stack = []
        for bracket in s:
            if stack and (stack[-1] == "(" and bracket == ")"):
                stack.pop()
            else:
                stack.append(bracket)

        return len(stack)