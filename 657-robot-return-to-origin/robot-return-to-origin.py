class Solution:
    def judgeCircle(self, moves: str) -> bool:
        vertical_sum = 0
        horizontal_sum = 0

        for move in moves:
            if move == "U":
                vertical_sum += 1
            elif move == "D":
                vertical_sum -= 1
            elif move == "R":
                horizontal_sum += 1
            elif move == "L":
                horizontal_sum -= 1

        return vertical_sum == 0 and horizontal_sum == 0