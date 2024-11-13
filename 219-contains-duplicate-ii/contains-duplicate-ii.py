class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        # i = 0
        # for j in range(i + 1, len(nums) - 1):  # To iterate starting from the second up to the last element
        #     while i < j and i < len(nums) - 2:   # To iterate until the entry before the last entry
        #         if nums[i] == nums[j] and abs(i - j) <= k:
        #             return True
        #         i += 1

        # else:
        #     return False

        # i, j = 0, 1
        # while i <= j < len(nums):
        #     if nums[i] == nums[j] and abs(i - j) <= k:
        #         return True
    
        #     j += 1
        #     if abs(i - j) > k:  # To check whether the difference of the pointers is less or equal to k
        #         i += 1
    
        # return False

        # 
        
        nums_dict = {}
        for index, val in enumerate(nums):
            if val in nums_dict and index - nums_dict[val] <= k:
                return True
            else:
                nums_dict[val] = index

        return False
            