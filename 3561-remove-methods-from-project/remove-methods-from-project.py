from collections import defaultdict
class Solution:
    def remainingMethods(self, n: int, k: int, invocations: List[List[int]]) -> List[int]:
        D={}
        for i in range(n):
            D[i]=[]
        for u,v in invocations:
            D[u].append(v)
        
        suspicious=set()
        def dfs(node,visited):
            visited.add(node)
            for nei in D[node]:
                if nei not in visited:
                    dfs(nei,visited)
        dfs(k,suspicious)

        not_suspicious=set()

        def dfs2(node,visited):
            visited.add(node)
            for nei in D[node]:
                if nei in suspicious:
                    return True
                if nei not in visited:
                    if dfs2(nei,visited):
                        return True
            return False
                
        for node in list(D):
            if node not in suspicious:
                if dfs2(node,not_suspicious):
                    return list(range(n))
        return list(not_suspicious)
        
