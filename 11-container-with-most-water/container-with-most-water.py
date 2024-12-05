class Solution:
    def maxArea(self, height: List[int]) -> int:
        
        # pointer_one = 0
        # pointer_two = len(height) - 1
        # pointer_two_clone = pointer_two
        # area_max = 0
        # height_taken = 0 # the appropriate height taken to get the area
        
        # # while pointer_one < pointer_two:
        # #     while pointer_two_clone > 0:
        # #         area = (height[pointer_one]) * (pointer_two_clone - pointer_one)
        # #         if area > area_max:
        # #             area_max = area
        # #         pointer_two_clone -= 1
        # #     pointer_one += 1

        # for i in range(pointer_two):
        #     for j in range(1, pointer_two + 1):
                
        #         if height[i] < height[j]:
        #             height_taken = height[i]
        #         else:
        #             height_taken = height[j]
                
        #         area = (height_taken) * (j - i) 
        #         if area > area_max:
        #             area_max = area

        # return area_max


        left = 0
        right = len(height) - 1
        max_area = 0

        while left < right:
            min_height = min(height[left], height[right])
            width = right - left

            area = min_height * width

            max_area = max(area, max_area)

            if height[left] < height[right]:
                left += 1

            elif height[left > height[right]]:
                right -= 1

            else:
                if height[left + 1] < height[right - 1]:
                    right -= 1
                else:
                    left += 1

        return max_area