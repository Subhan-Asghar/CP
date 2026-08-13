import math
class Solution:
    def numSquares(self, n: int) -> int:
        nums=[]
        i=1
        while i*i<=n:
            nums.append(i*i)
            i+=1
        W=n
        memo={}
        def solve(W):
            if W==0:
                return 0

            if W in memo:
                return memo[W]

            ans=float('inf')

            for n in nums:
                if n>W:
                    break
                take=1+solve(W-n)
                ans=min(ans,take)
            memo[W]=ans
            return ans
        return solve(W)