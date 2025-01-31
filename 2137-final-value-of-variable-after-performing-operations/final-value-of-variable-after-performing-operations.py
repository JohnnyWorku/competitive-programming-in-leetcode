class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        x = 0
        for char in operations:
            if char == "++X" or char == "X++":
                x += 1
            else:
                x -= 1

        return x