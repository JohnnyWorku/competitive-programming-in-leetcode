class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        i = 0
        count = {}
        longest = 0

        for j in range(len(s)):
            count[s[j]] = 1 + count.get(s[j], 0)

            if (j - i + 1) - max(count.values()) > k:
                count[s[i]] -= 1
                i += 1

            longest = max(longest, j - i + 1)

        return longest
        