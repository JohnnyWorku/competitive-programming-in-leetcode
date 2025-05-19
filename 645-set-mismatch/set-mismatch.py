class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        # i = 0
        # while i < len(nums):
        #     if nums[i] == nums[nums[i] - 1]:
        #         i += 1
        #         continue
        #     if nums[i] != i + 1:
        #         temp = nums[i] - 1
        #         nums[temp], nums[i] = nums[i], nums[temp]
        #     if nums[i] == i + 1:
        #         i += 1

        # errors = []
        # for j in range(len(nums)):
        #     if nums[j] != j + 1:
        #         errors.append(nums[j])
        #         errors.append(j + 1)

        # return errors

        i = 0
        while i < len(nums):
            if nums[i] != i + 1:
                temp_index = nums[i] - 1
                if nums[temp_index] != nums[i]:
                    nums[temp_index], nums[i] = nums[i], nums[temp_index]
                else:
                    i += 1
            else:
                i += 1

        for i in range(len(nums)):
            if nums[i] != i + 1:
                return [nums[i], i + 1]
