class Solution:
    def constructTransformedArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = []

        for i in range(n):
            if nums[i] == 0:
                result.append(nums[i])
            else:
                index = (i + nums[i]) % n  #to make circular
                no_to_append = nums[index] 
                result.append(no_to_append)

        return result
