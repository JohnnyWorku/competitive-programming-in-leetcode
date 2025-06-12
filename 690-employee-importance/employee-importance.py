"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        graph = defaultdict(list)
        for employee in employees:
            graph[employee.id].append((employee.importance, employee.subordinates))

        visited = set()
        total_importance = 0

        def dfs(id):
            nonlocal total_importance

            visited.add(id)
            importance, subordinates = graph[id][0]
            for subordinate in subordinates:
                if subordinate not in visited:
                    dfs(subordinate)
            
            total_importance += importance

        dfs(id)

        return total_importance
        