class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:

        nums.sort()  # Sort the list
        result = []
        n = len(nums)

        # Iterate through possible first numbers (i) and last numbers (l)
        for i in range(n - 3):
            # Skip duplicate elements for i
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            for l in range(n - 1, i + 2, -1):
                # Skip duplicate elements for l
                if l < n - 1 and nums[l] == nums[l + 1]:
                    continue

                # Set two pointers
                j, k = i + 1, l - 1
                while j < k:
                    # Calculate the sum of the four elements
                    total = nums[i] + nums[j] + nums[k] + nums[l]
                    
                    if total == target:
                        result.append([nums[i], nums[j], nums[k], nums[l]])

                        # Skip duplicates for j and k
                        while j < k and nums[j] == nums[j + 1]:
                            j += 1
                        while j < k and nums[k] == nums[k - 1]:
                            k -= 1

                        # Move pointers
                        j += 1
                        k -= 1
                    elif total < target:
                        j += 1
                    else:
                        k -= 1

        return result
