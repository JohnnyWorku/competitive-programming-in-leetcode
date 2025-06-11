class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        color = [-1 for _ in range(len(graph))]

        def dfs(node, current_color):
            color[node] = current_color

            for neighbour in graph[node]:
                if color[neighbour] == -1:
                    if not dfs(neighbour, 1 - current_color):
                        return False
                elif color[neighbour] == current_color:
                    return False

            return True

        for i in range(len(graph)):
            if color[i] == -1:
                if not dfs(i, 0):
                    return False

        return True
        