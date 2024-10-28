class Solution:
    def isPossibleToSplit(self, nums: List[int]) -> bool:
        nums_dict = {}

        for num in nums:
            if nums_dict.get(num):
                nums_dict[num] += 1
            else:
                nums_dict[num] = 1

        for count in nums_dict.values():
            if count > 2:
                return False

        return True
