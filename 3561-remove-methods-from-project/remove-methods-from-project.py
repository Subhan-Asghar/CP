from collections import defaultdict
class Solution:
    def remainingMethods(self, n: int, k: int, invocations: List[List[int]]) -> List[int]:
        D=defaultdict(list)
        for u,v in invocations:
            D[u].append(v)

        suspicious=set()

        def dfs(node,visited):
            visited.add(node)
            for nei in D[node]:
                if nei not in visited:
                    dfs(nei,visited)
        dfs(k,suspicious)
    
        for u,v in invocations:
            if u not in suspicious and v in suspicious:
                return list(range(n))
        return [i for i in range(n) if i not in suspicious]

