class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        # It is sorted because we get the optimal solution when we pair small numbers with other small numbers and large numbers with other large numbers
        nums.sort()
        total = 0

        for i in range(0, len(nums), 2):
            total += min(nums[i], nums[i + 1])

        return total