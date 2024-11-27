class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        current_sum = 0
        # max_average = - float('inf')
        i = 0

        for j in range(k):
            current_sum += nums[j]

        max_average = current_sum / k
        j += 1

        while j < len(nums):
            current_sum += nums[j] - nums[i]
            i += 1
            j += 1
            average = current_sum / k
            max_average = max(max_average, average)
            

        return max_average
