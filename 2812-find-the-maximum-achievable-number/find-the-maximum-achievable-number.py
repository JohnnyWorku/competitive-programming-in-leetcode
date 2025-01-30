class Solution:
    def theMaximumAchievableX(self, num: int, t: int) -> int:
        # The maximum achievable no will gotten after knowing how many 1s to add on or subtract from num and same thing on x
        max_no = num + (t * 2)
        return max_no