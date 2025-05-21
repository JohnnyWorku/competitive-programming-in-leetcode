class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        # trust_graph = [set() for _ in range(n)]
        
        # for a, b in trust:
        #     trust_graph[a - 1].add(b)

        # candidate = 0
        # for j in range(n):
        #     if not trust_graph[j]:
        #         candidate =  j + 1

        # for k in range(n):
        #     if k == candidate - 1:
        #         continue
        #     if candidate not in trust_graph[k]:
        #         return -1

        # return candidate

        incoming_edges = {n : 0 for n in range(1, n + 1)}
        outgoing_edges = {n : 0 for n in range(1, n + 1)}

        for a, b in trust:
            incoming_edges[b] += 1
            outgoing_edges[a] += 1

        for node, edges in incoming_edges.items():
            if edges == n - 1 and outgoing_edges[node] == 0:
                return node

        return -1
        