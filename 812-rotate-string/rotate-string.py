class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        s_updated = s + s

        if len(goal) == len(s) and goal in s_updated:
            return True

        return False