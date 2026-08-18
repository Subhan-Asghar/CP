class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        memo={}
        def solve(l,r):
            if l>=r:
                return 0
            if (l,r) in memo:
                return memo[(l,r)]
            first=piles[l]-solve(l+1,r)
            last=piles[r]-solve(l,r-1)
            ans=max(first,last)
            memo[(l,r)]=ans
            return ans

        return solve(0,len(piles)-1)>=0