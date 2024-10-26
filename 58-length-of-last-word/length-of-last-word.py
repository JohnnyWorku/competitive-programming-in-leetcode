class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s1 = s.strip()
        splited = s1.split(" ")
        return len(splited[-1])

        