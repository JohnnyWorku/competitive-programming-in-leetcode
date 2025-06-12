class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        ## Using dfs cycle detection method

        # Color representations
        # -1 - white
        # 0 - gray
        # 1 - black

        graph = [[] for _ in range(numCourses)]
        colors = [-1 for _ in range(numCourses)]

        for course, prereq in prerequisites:
            graph[course].append(prereq)

        no_cycle = True
        def dfs(node):
            nonlocal no_cycle

            if not no_cycle:
                return

            colors[node] = 0
            for neighbour in graph[node]:
                if colors[neighbour] == -1:
                    dfs(neighbour)
                elif colors[neighbour] == 0:
                    no_cycle = False

            colors[node] = 1

        for course in range(numCourses):
            if colors[course] == -1:
                dfs(course)

        return no_cycle
        