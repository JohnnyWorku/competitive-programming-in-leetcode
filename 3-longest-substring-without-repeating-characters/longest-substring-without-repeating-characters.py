class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i = 0
        j = 1
        longest = 0

        if len(s) == 0:
            return 0

        elif len(s) == 1:
            return 1

        while j < len(s):
            if s[j] not in s[i: j]:
                longest = max(longest, j - i + 1)
                j += 1

            else:
                i += 1

        return longest