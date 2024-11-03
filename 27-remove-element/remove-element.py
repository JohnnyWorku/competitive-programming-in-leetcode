class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0  # Initialize the index counter
    
        while k < len(nums):
            if nums[k] == val:
                nums.pop(k)  # Remove the element if it matches `val`
            else:
                k += 1  # Only increment `k` if we don't remove an element
        
        return len(nums)




