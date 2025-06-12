class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        ROWS, COLS = len(isConnected), len(isConnected)

        graph = defaultdict(set)
        for row in range(ROWS):
            for col in range(COLS):
                if isConnected[row][col]:
                    graph[row].add(col)
                    graph[col].add(row)

        visited = set()
        def dfs(node):
            visited.add(node)

            for neighbour in graph[node]:
                if neighbour not in visited:
                    dfs(neighbour)

        provinces = 0
        for node in graph:
            if node not in visited:
                dfs(node)
                provinces += 1

        return provinces
        