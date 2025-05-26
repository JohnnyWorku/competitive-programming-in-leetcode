class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        # Using cyclic sort
        i = 0
        while i < len(nums):
            if nums[i] == nums[nums[i] - 1]:
                i += 1
                continue
            if nums[i] != i + 1:
                temp = nums[i] - 1
                nums[temp], nums[i] = nums[i], nums[temp]
            if nums[i] == i + 1:
                i += 1

        duplicates = []
        for j in range(len(nums)):
            if nums[j] != j + 1:
                duplicates.append(nums[j])
        duplicates.sort()

        return duplicates

        # Using hash table (conter dictionary)
        res = []
        counter = Counter(nums)
        for num, appearance in counter.items():
            if appearance == 2:
                res.append(num)

        return res
