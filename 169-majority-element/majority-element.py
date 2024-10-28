class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums_dict = {}

        for num in nums:
            if nums_dict.get(num):
                nums_dict[num] += 1
            else:
                nums_dict[num] = 1

        maximum = nums_dict[num]
        frequent_num = num
        for number in nums_dict:
            if nums_dict[number] > maximum:
                maximum = nums_dict[number]
                frequent_num = number

        return frequent_num

            