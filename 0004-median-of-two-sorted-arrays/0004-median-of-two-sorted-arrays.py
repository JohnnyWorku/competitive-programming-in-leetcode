class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        new_nums = []
        for num1 in nums1:
            new_nums.append(num1)
        for num2 in nums2:
            new_nums.append(num2)
        new_nums.sort()
        left = 0
        right = len(new_nums) - 1
        middle = (left + right) // 2
        if len(new_nums) % 2 != 0:
            return float(new_nums[middle])
        else:
            return float((new_nums[middle] + new_nums[middle + 1]) / 2)

