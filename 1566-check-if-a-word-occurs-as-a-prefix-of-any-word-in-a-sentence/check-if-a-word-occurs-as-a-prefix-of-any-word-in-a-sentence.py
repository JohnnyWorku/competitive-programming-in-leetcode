class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        sentence_list = sentence.split()

        for word in sentence_list:
            if word[:len(searchWord)] == searchWord:
                return (sentence_list.index(word) + 1)

        return -1