class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        counter = 0
        i = 0
        j = 1
        while i < j < len(nums):
            if j != len(nums) - 1:
                if nums[i] == nums[j] and i < j:
                    counter += 1
                j += 1

            else:
                if nums[i] == nums[j] and i < j:
                    counter += 1
                i += 1
                j = i + 1

        return counter
