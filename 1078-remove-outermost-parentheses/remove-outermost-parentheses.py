class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        result = ""
        outer_level = 0  # Tracks the nesting level to detect outermost brackets

        for bracket in s:
            if bracket == "(":
                if outer_level > 0:  # Only add '(' to result if it’s not outermost
                    result += "("
                outer_level += 1
            elif bracket == ")":
                outer_level -= 1
                if outer_level > 0:  # Only add ')' to result if it’s not outermost
                    result += ")"

        return result
