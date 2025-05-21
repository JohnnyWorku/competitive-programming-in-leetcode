class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        # We use multisource BFS
        rows, cols = len(isWater), len(isWater[0])
        res = [[-1 for _ in range(cols)] for _ in range(rows)]
        queue = deque()

        # Inbound checker
        def inbound(row, col):
            return 0 <= row < rows and 0 <= col < cols

        # Enqueue water parts
        for row in range(rows):
            for col in range(cols):
                if isWater[row][col]:
                    res[row][col] = 0
                    queue.append((row, col))

        while queue:
            r, c = queue.popleft()
            h = res [r][c]

            neighbours = [(r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)]

            for nr, nc in neighbours:
                # First check if it is inbound and not visited(check if its value is -1)
                if inbound(nr, nc) and res[nr][nc] == -1:
                    res[nr][nc] = h + 1
                    queue.append((nr, nc))

        return res
        