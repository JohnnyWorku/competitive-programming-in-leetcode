class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels_list = ['a', 'e', 'i', 'o', 'u']
        s = list(s)
        i = 0
        j = len(s) - 1

        while i <= j: 
            if s[i].lower() in vowels_list and s[j].lower() in vowels_list:
                s[i], s[j] = s[j], s[i]
                i += 1
                j -= 1
            elif s[i].lower() in vowels_list and s[j].lower() not in vowels_list:
                j -= 1
            elif s[i].lower() not in vowels_list and s[j].lower() in vowels_list:
                i += 1
            else:
                i += 1
                j -= 1

        s = "".join(s)

        return s