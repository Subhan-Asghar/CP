class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        r=len(obstacleGrid)
        c=len(obstacleGrid[0])
        if obstacleGrid[r-1][c-1]==1:
            return 0
        memo={}
        def solve(i,j):
            if (i,j) in memo:
                return memo[(i,j)]
            if i<0 or j<0 or i>=r or j>=c or obstacleGrid[i][j]==1:
                return 0
            if i==r-1 and j==c-1:
                return 1
            down=solve(i+1,j)
            right=solve(i,j+1)
            ans=down+right
            memo[(i,j)]=ans
            return ans
        return solve(0,0)
            