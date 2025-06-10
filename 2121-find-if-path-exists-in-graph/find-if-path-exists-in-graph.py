class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph = defaultdict(list)
        for edge in edges:
            node1, node2 = edge[0], edge[1]
            graph[node1].append(node2)
            graph[node2].append(node1)

        ## Recursive way

        # visited = set()
        # def dfs(node, visited):
        #     if node == destination:
        #         return True

        #     visited.add(node)
        #     for neighbour in graph[node]:
        #         if neighbour not in visited:
        #             if dfs(neighbour, visited):
        #                 return True
            
        #     return False

        # return dfs(source, visited)

        ## Iterative way
        visited = set([source])
        stack = [source]

        while stack:
            node = stack.pop()
            if node == destination:
                return True

            for neighbour in graph[node]:
                if neighbour not in visited:
                    visited.add(neighbour)
                    stack.append(neighbour)

        return False
        