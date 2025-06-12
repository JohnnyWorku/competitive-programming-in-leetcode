class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        directions = [(0, -1), (0, 1), (1, 0), (-1, 0)]
        visited = set()

        def in_bound(row, col):
            return 0 <= row < ROWS and 0 <= col < COLS

        def dfs(row, col):
            nonlocal curr_area
            visited.add((row, col))

            for hor, ver in directions:
                new_row = row + hor
                new_col = col + ver

                if in_bound(new_row, new_col) and (new_row, new_col) not in visited and grid[new_row][new_col] == 1:    
                    dfs(new_row, new_col)
                    curr_area += 1

        max_area = -float("inf")
        for row in range(ROWS):
            for col in range(COLS):
                if (row, col) not in visited and grid[row][col]:
                    curr_area = 1
                    dfs(row, col)
                    max_area = max(max_area, curr_area)

        return 0 if max_area == -float("inf") else max_area
        