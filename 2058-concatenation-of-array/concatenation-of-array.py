class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        # nums.extend(nums)
        ans = nums + nums
        return ans