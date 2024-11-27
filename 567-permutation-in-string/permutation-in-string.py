class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_count = Counter(s1)
        i = 0
        j = len(s1) - 1

        while j < len(s2):
            s2_count = Counter(s2[i: j + 1])
            if s1_count == s2_count:
                return True

            i += 1
            j += 1

        return False