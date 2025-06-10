class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]
        visited = [[False for _ in range(COLS)] for _ in range(ROWS)]

        def in_bound(row, col):
            return 0 <= row < ROWS and 0 <= col < COLS

        perimeter = 0
        def dfs(row, col):
            nonlocal perimeter
            
            visited[row][col] = True

            for hor, ver in directions:
                new_row = row + hor
                new_col = col + ver

                if in_bound(new_row, new_col) and grid[new_row][new_col]:
                    if not visited[new_row][new_col]:
                        dfs(new_row, new_col)
                else:
                    perimeter += 1

            return perimeter

        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col]:
                    return dfs(row, col)
        