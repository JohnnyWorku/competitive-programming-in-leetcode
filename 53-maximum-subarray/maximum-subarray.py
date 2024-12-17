class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        total = 0
        result = nums[0]

        for num in nums:
            if total >= 0:
                total += num

            else:
                total = 0
                total += num

            if total > result:
                result = total

        return result
        
        

