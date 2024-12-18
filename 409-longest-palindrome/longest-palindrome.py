class Solution:
    def longestPalindrome(self, s: str) -> int:
        seen = set()
        count = 0

        for char in s:
            if char in seen:
                seen.remove(char)
                count += 2  # To track the previous and also this one
            else:
                seen.add(char)

        return count + 1 if seen else count

        

            