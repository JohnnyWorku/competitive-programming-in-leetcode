class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # pref = strs[0]
        # pref_len = len(pref)

        # for s in strs[1 : ]:
        #     while pref != s[0 : pref_len]:
        #         pref_len -= 1
        #         pref = pref[0: pref_len]
                
        #         if pref_len == 0:
        #             return ""

        # return pref[0 : pref_len]
        count = 0
        strs = sorted(strs, key=len)
        # print(strs)
        first_str = strs[0]
        common_prefix = ""

        for i in range(len(first_str)):
            for word in strs:
                if first_str[i] == word[i]:
                    count += 1

            if count == len(strs):
                common_prefix += first_str[i]
                count = 0

            else:
                return common_prefix

        return common_prefix
