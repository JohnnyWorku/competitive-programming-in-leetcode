class Solution:
    def getLucky(self, s: str, k: int) -> int:
        letters = ["a", "b", "c", "d", "e", "f", "g", "h", 
                    "i", "j", "k", "l", "m", "n", "o", "p", 
                    "q", "r", "s", "t", "u", "v", "w", "x", 
                    "y", "z"]

        numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13,
                    14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24,
                    25, 26]

        num_representation = ""

        for letter in s:
            num_representation += str(numbers[letters.index(letter)])

        for i in range(k):
            summation = 0
            for num in num_representation:
                summation += int(num)

            num_representation = str(summation)


        return int(num_representation)
