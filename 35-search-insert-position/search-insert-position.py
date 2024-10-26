class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        # if target in nums:
        #     return nums.index(target)
        # else:
        #     new_nums = []
        #     for num in nums:
        #         if num < target:
        #             new_nums.append(num)
        #     new_nums.append(target)
        #     return new_nums.index(target) 

        low = 0
        high = len(nums) - 1

        while low <= high:
            mid = (low + high) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                low = mid + 1
            else:
                high = mid - 1

        # If the number is not in the array
        for i in range(len(nums) - 1):
            if nums[i] < target < nums[i + 1]:
                return i + 1

        if target > nums[-1]:
            return len(nums)
        elif target < nums[0]:
            return 0



            