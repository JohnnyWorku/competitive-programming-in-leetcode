class Solution:
    def sumOfThree(self, num: int) -> List[int]:
        # Let: the first_no = x
        #      the second_no = x + 1
        #      the third_no = x + 2
        # and use x + (x + 1) + (x + 2) = num
        # 3x = num - 3
        # x = (num - 3) // 3
        
        x = (num - 3) // 3

        if x + (x + 1) + (x + 2) == num:
            return [x, x + 1, x + 2]
        
        return []

        