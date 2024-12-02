class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        total = sum(nums)
        left_sum = nums[0]
        counter = 0

        for i in range(1, len(nums)):
            right_sum = total - left_sum

            if left_sum >= right_sum:
                counter += 1

            left_sum += nums[i]

        return counter