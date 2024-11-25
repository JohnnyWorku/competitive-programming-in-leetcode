class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # index_1 = 0
        # index_2 = len(nums) - 1
        # solution = []

        # while index_1 <= index_2:
        #     summation = nums[index_1] + nums[index_2]
        #     if summation >= 0:
        #         if summation < target:
        #             index_1 += 1
        #         elif summation > target:
        #             index_2 -= 1

        #     else:
        #         if summation > target:
        #             index_1 += 1
        #         elif summation < target:
        #             index_2 -= 1

        # solution.append(index_1)
        # solution.append(index_2)
        # return solution

        num_index_dict = {}

        for index, num in enumerate(nums):
            if target - num in num_index_dict:
                return [index, num_index_dict[target - num]]

            num_index_dict[num] = index