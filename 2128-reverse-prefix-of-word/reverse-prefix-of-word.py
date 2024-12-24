class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        new_word = ""

        for r in range(len(word)):
            if word[r] == ch:
                new_word += word[: r + 1][::-1] + word[r + 1:]
                return new_word

        return word