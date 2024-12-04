class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        i = 0
        _sum = 0
        max_sum = - float('inf')

        for j in range(len(nums)):
            _sum += nums[j]

            if (j - i + 1) == k:
                max_sum = max(max_sum, _sum)
                _sum -= nums[i]
                i += 1

        max_average = max_sum / k

        return max_average