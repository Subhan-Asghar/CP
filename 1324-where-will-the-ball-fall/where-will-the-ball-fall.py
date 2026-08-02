from collections import deque
class Solution:
    def findBall(self, grid: List[List[int]]) -> List[int]:
        r=len(grid)
        c=len(grid[0])
        def check(i,j):
            q=deque([(i,j)])
            while q:
                qr,qc=q.popleft()
                if qr>=r:
                    return qc
               
                direction=grid[qr][qc]
                if direction==1:
                    
                    if qc+1>=c or grid[qr][qc+1]==-1:
                        return -1
                    q.append((qr+1,qc+1))
                else:
                    if qc-1<0 or grid[qr][qc-1]==1:
                        return -1
                    q.append((qr+1,qc-1))
            return -1

        result=[]
        for i in range(c):
            result.append(check(0,i))
        return result