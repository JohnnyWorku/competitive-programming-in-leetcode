class Solution:
    def maxDepth(self, s: str) -> int:
        bracket_dict = {"(": ")"}
        stack = []
        count = 0
        max_count = 0

        for char in s:
            if char == "(":
                stack.append(char)
                count += 1

            elif char == ")":
                max_count = max(max_count, count)
                stack.pop()
                count -= 1

        return max_count
