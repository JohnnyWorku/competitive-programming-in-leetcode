class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # shortest = min(strs, key = len)
        len_shortest = float('inf')
        shortest = ""
        for string in strs:
            if len(string) <= len_shortest:
                len_shortest = len(string)
                shortest = string
        
        common_prefix = ""
        count = 0

        for i in range(len(shortest)):
            for str in strs:
                if str[i] == shortest[i]:
                    count += 1

            if count == len(strs):
                count = 0
                common_prefix += shortest[i]

            else:
                break

        return common_prefix