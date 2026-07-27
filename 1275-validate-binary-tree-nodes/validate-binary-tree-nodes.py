from collections import defaultdict ,deque
class Solution:
    def validateBinaryTreeNodes(self, n: int, leftChild: List[int], rightChild: List[int]) -> bool:
        D=defaultdict(list)
        for i in range(n):
            if leftChild[i]!=-1:
                D[i].append(leftChild[i])
            if rightChild[i]!=-1:
                D[i].append(rightChild[i])
        indegree=[0]*n
        for node in D:
            for nei in D[node]:
                indegree[nei]+=1
        source=-1
        for i in range(n):
            if indegree[i]==0:
                source=i
        if source==-1:
            return False
        visited=set()
        visited.add(source)
        q=deque([source])
        while q:
            node=q.popleft()
            
            for nei in D[node]:
                if nei in visited:
                    return False
                q.append(nei)
                visited.add(nei)
        return len(visited)==n