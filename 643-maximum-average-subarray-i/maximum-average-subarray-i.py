class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        current_sum = sum(nums[:k])
        max_average = current_sum / k
        i = 0
        j = i + k

        while j < len(nums):
            current_sum += nums[j] - nums[i]
            i += 1
            j += 1
            average = current_sum / k
            max_average = max(max_average, average)
            

        return max_average
