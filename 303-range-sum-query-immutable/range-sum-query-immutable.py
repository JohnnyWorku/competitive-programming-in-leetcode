class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums
        self.prefix_sum = []

        self.prefix_sum.append(self.nums[0])
        
        for i in range(1, len(self.nums)):
            self.prefix_sum.append((self.prefix_sum[i - 1] + self.nums[i]))
        

    def sumRange(self, left: int, right: int) -> int:
        right = self.prefix_sum[right]
        left = self.prefix_sum[left - 1] if left != 0 else 0 

        return right - left


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)