class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        # i, j = 0, 1
        # minimum = float('inf')
        # summation = nums[i]
        # while i <= j < len(nums):
        #     if summation < target:
        #         summation += nums[j]
        #         j += 1

        #     else:
        #         summation -= nums[i]
        #         i += 1

        #     if (j - i + 1) < minimum:
        #         minimum = j - i 

        # return minimum

        i = 0
        current_sum = 0
        shortest = float('inf')

        for j in range(len(nums)):
            current_sum += nums[j]

            while current_sum >= target:
                shortest = min(shortest, j - i + 1)
                current_sum -= nums[i]
                i += 1

        return shortest if shortest != float('inf') else 0