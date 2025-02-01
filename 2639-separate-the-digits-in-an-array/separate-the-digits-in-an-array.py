class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        answer = []
        for num in nums:
            num = str(num)
            for n in num:
                answer.append(int(n))

        return answer
