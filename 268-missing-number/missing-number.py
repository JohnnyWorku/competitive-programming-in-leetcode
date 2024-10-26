class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        i = 0
        while i < len(nums):
            if nums[i] >= len(nums):
                i += 1
                continue
            if nums[i] != i:
                temp_index = nums[i]
                nums[temp_index], nums[i] = nums[i], nums[temp_index]  # swapping
            if nums[i] == i:      # To check if the swapped position is the correct position
                i += 1

        for j in range(len(nums)):
            if nums[j] != j:
                return j
        return len(nums)
        