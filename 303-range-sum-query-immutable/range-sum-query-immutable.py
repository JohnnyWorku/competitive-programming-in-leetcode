class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums
        self.prefix_sum = []
        for _ in range(len(self.nums)):
            self.prefix_sum.append(0)

    def sumRange(self, left: int, right: int) -> int:
        self.prefix_sum[left] = self.nums[left]
        for i in range(left + 1, right + 1):
            self.prefix_sum[i] = self.prefix_sum[i - 1] + self.nums[i]

        return self.prefix_sum[right]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)