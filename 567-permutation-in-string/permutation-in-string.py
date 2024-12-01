class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        i = 0
        j = i + len(s1) - 1
        s1_counter = Counter(s1)

        while j < len(s2):
            s2_counter = Counter(s2[i: j + 1])

            if s1_counter == s2_counter:
                return True

            else:
                i += 1
                j += 1

        return False
