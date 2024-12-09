class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        seen, result = set(), set()

        for i in range(len(s) - 9): # To left the last ten elements
            cur = s[i: i + 10]
            if cur in seen:
                result.add(cur)
            seen.add(cur)

        return list(result)
