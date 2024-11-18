class Solution:
    def findLHS(self, nums: List[int]) -> int:
        # nums = sorted(nums)
        # i = 0
        # counter = 0

        # for j in range(1, len(nums)):
        # # Ensure the subarray nums[i:j+1] has a difference of at most 1 between max and min
        #     while nums[j] - nums[i] > 1:
        #         i += 1  # Shrink the window from the left

        # # Update the counter to store the maximum length of valid subarray
        #     counter = max(counter, j - i + 1)
    
        # return counter

        nums = sorted(nums)
        nums_dict = {}

        for num in nums:
            if nums_dict.get(num):
                nums_dict[num] += 1
            else:
                nums_dict[num] = 1

        counter = 0

        nums = list(nums_dict.items())
        for i in range(len(nums) - 1):
            if nums[i + 1][0] - nums[i][0] == 1: 
                counter = max(counter, (nums[i][-1] + nums[i + 1][-1]))

        return counter
