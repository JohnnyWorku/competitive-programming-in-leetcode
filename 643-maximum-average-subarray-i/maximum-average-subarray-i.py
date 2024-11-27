class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        n = len(nums)
        current_sum = 0
        for i in range(k):
            current_sum += nums[i]

        max_average = current_sum / k

        for i in range(k, n):
            current_sum += nums[i] - nums[i - k]
            average = current_sum / k
            max_average = max(max_average, average)

        return max_average
