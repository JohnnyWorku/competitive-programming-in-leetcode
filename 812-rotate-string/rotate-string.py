class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        # The efficient one
        return len(s) == len(goal) and goal in (s + s)

        # s_updated = s + s

        # if len(goal) == len(s) and goal in s_updated:
        #     return True

        # return False