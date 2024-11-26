class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        max_area = 0

        # Brute Force
        # while left < len(height):
        #     for right in range(len(height)):
        #         area = min(height[left], height[right]) * (right - left)
        #         max_area = max(max_area, area)

        #     left += 1

        # return max_area

        while left < right:
            area = min(height[left], height[right]) * (right - left)
            max_area = max(max_area, area)

            if height[left] < height[right]:
                left += 1
            elif height[left] > height[right]:
                right -= 1
            else:
                if height[left + 1] < height[right - 1]:
                    right -= 1
                else:
                    left += 1

        return max_area