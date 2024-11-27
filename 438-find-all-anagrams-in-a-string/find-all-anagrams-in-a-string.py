class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        i = 0
        j = len(p) - 1
        start_indices = []

        p_count = Counter(p)

        while j < len(s):
            s_count = Counter(s[i: j + 1])
            if p_count == s_count:
                start_indices.append(i)

            i += 1
            j += 1

        return start_indices
        