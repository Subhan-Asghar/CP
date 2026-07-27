class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        r=len(board)
        c=len(board[0])
        directions=[(1,0),(0,1),(-1,0),(0,-1)]
        def dfs(i,j,index):
            if index==len(word):
                return True
            if i<0 or j<0 or i>=r or j>=c or (i,j) in visited:
                return False
            if board[i][j]==word[index]:
                visited.add((i,j))
                for dr,dc in directions:
                    nr=dr+i 
                    nc=dc+j
                    if dfs(nr,nc,index+1):
                        return True 
                visited.remove((i,j))
            return False
        for i in range(r):
            for j in range(c):
                if board[i][j]==word[0]:
                    visited=set()
                    if dfs(i,j,0):
                        return True
        return False