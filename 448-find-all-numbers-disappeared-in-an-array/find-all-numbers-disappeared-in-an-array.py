class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        # i = 0
        # while i < len(nums):
        #     if nums[i] == nums[nums[i] - 1]:  # To check whether the values duplicate is already at the correct position or not.
        #         i += 1
        #         continue
        #     if nums[i] != i + 1:
        #         temp_index = nums[i] - 1
        #         nums[temp_index], nums[i] = nums[i], nums[temp_index]  # swapping
        #     if nums[i] == i + 1:  # To check if the swapped position is the correct position
        #         i += 1

        # missed_numbers = []
        # for j in range(len(nums)):
        #     if nums[j] != j + 1:
        #         missed_numbers.append(j + 1)

        # for k in range(len(nums)):
        #     if nums[k] == k + 1 and len(missed_numbers) == 0:
        #         return []

        # if len(missed_numbers) != 0:
        #     return missed_numbers

        # else:
        #     missed_numbers.append(len(nums))
        #     return missed_numbers

        nums_set = set(n for n in range(1, len(nums) + 1))
        print(nums_set)
        for num in nums:
            if num in nums_set:
                nums_set.remove(num)

        return list(nums_set)
