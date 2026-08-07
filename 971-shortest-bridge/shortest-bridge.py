from collections import deque
class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        r=len(grid)
        c=len(grid[0])
        directions=[(1,0),(0,1),(0,-1),(-1,0)]
        def dfs(i,j):
            if i<0 or j<0 or i>=r or j>=c or (i,j) in visited or grid[i][j]!=1:
                return 
            visited.add((i,j))
            for dr,dc in directions:
                nr=i+dr
                nc=j+dc
                dfs(nr,nc)
        visited=set()
        def get_index():
            for i in range(r):
                for j in range(c):
                    if grid[i][j]==1:
                        return [i,j]

        i,j=get_index()
        dfs(i,j)
        q=deque(list(visited))
        level=0

        while q:
            n=len(q)
            for _ in range(n):
                qr,qc=q.popleft()
                for dr,dc in directions:
                    nr=dr+qr
                    nc=dc+qc
                    if 0<=nr<r and 0<=nc<c and (nr,nc) not in visited:
                        if grid[nr][nc]==1:
                            return level
                        q.append((nr,nc))
                        visited.add((nr,nc))
            level+=1
        return level