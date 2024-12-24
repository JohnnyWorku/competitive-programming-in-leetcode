class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        for i in range(len(word)):
            if word[i] == ch:
                new_word = word[:i + 1][::-1] + word[i + 1:]
                return new_word

        return word