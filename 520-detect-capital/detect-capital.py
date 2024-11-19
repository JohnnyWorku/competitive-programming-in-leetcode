class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        count = 0
        i = 0

        # if len(word) == 1:
        #     return True

        while i < len(word):
            if word[i].isupper():
                count += 1
            i += 1

        if count == i or count == 0:  # This means all are capital or all small
            return True

        elif word[0].isupper() and count == 1:  # This means only the first one is capital
            return True
        
        return False
    