class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        counter = {}
        for num in nums:
            counter[num] = 0
        distinct_nums = 0
        count = 0

        left = 0
        for right in range(len(nums)):
            num = nums[right]
            if counter[num] == 0:
                distinct_nums += 1
            counter[num] += 1
            
            while distinct_nums == len(counter):
                count += len(nums) - right
                counter[nums[left]] -= 1
                if counter[nums[left]] == 0:
                    distinct_nums -= 1
                left += 1

        return count
        