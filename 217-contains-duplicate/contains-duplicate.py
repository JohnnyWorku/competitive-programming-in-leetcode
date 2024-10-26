class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums = sorted(nums)
        i = 0
        j = 1
        while i <= j < len(nums):
            if nums[i] == nums[j]:
                return True
            else:
                i += 1
                j += 1

        return False
        