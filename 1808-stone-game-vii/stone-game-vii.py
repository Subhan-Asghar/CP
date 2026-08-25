class Solution:
    def stoneGameVII(self, stones: List[int]) -> int:
        n=len(stones)
        prefix=[0]*n
        prefix[0]=stones[0]

        for i in range(1,n):
            prefix[i]=prefix[i-1]+stones[i]
        memo=[[None]*n for _ in range(n)]
        def solve(l,r):
            if l>=r:
                return 0
            if memo[l][r] is not None:
                return memo[l][r]
            if l==0:
                val=prefix[r]
            else:
                val=prefix[r]-prefix[l-1]
            left=(val-stones[l])-solve(l+1,r)
            right=(val-stones[r])-solve(l,r-1)
            ans=max(left,right)
            memo[l][r]=ans
            return ans
        return solve(0,n-1)
        