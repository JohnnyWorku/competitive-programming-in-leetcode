class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        num_dict = Counter(nums)
        ans = []
        
        for i in num_dict:
            if num_dict[i] > math.floor(len(nums) / 3):
                ans.append(i)
        
        return ans