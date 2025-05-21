class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        trust_graph = [set() for _ in range(n)]
        
        for a, b in trust:
            trust_graph[a - 1].add(b)

        candidate = 0
        for j in range(n):
            if not trust_graph[j]:
                candidate =  j + 1

        for k in range(n):
            if k == candidate - 1:
                continue
            if candidate not in trust_graph[k]:
                return -1

        return candidate
        