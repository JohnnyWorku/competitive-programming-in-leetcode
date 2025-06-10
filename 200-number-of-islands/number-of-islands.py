class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        visited = set()

        def in_bound(row, col):
            return 0 <= row < ROWS and 0 <= col < COLS

        def dfs(row, col):
            visited.add((row, col))

            for hor, ver in directions:
                new_row = row + hor
                new_col = col + ver

                if in_bound(new_row, new_col) and grid[row][col] == "1" and (new_row, new_col) not in visited:
                    dfs(new_row, new_col)

        islands = 0
        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == "1" and (row, col) not in visited:
                    dfs(row, col)
                    islands += 1

        return islands
        