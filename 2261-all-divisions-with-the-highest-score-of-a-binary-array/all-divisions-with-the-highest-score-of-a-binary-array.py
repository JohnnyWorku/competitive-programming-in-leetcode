class Solution:
    def maxScoreIndices(self, nums: List[int]) -> List[int]:
        sum_scores = []
        res = []
        # This two(below) handle the case at index 0 - when nums_left = 0 and nums_right have all the count of ones
        zeros_left = 0
        ones_right = nums.count(1)
        sum_scores.append(zeros_left + ones_right)

        for i in range(1, len(nums)):
            if nums[i - 1] == 0:
                zeros_left += 1
            else:
                ones_right -= 1

            sum_scores.append(zeros_left + ones_right)

        # This is to handle the case of the last index
        if nums[-1] == 0:
            zeros_left += 1
        ones_right = 0

        sum_scores.append(zeros_left + ones_right)

        max_sum = max(sum_scores)

        for j in range(len(sum_scores)):
            if sum_scores[j] == max_sum:
                res.append(j)

        return res
