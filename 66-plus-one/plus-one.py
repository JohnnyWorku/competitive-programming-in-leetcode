class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        # number = 0
        # for num in digits:
        #     number = number * 10 + num
        # number += 1
        # number_string = list(map(int, str(number)))
        # return number_string
        num = 0
        ans = []
        for n in digits:
            num = num * 10 + n

        num += 1

        for number in str(num):
            ans.append(int(number))

        return ans
