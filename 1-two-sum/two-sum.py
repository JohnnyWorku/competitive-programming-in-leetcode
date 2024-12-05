class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_dict = {}

        for index, num in enumerate(nums):
            if target - num in nums_dict:
                return [index, nums_dict.get(target - num)]

            nums_dict[num] = index