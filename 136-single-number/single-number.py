class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        for num in nums:
            if num not in nums[nums.index(num) + 1 : ]:
                return num
        