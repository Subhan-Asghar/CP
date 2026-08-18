class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        memo={}
        def solve(l,r):
            if l>r: return 0
            if l==r: return 1
            ans=0
            if (l,r) in memo:
                return memo[(l,r)]
            if s[l]==s[r]:
                ans=2+solve(l+1,r-1)      
            else:
                ans=max(solve(l+1,r),solve(l,r-1))
            memo[(l,r)]=ans
            return ans
        return solve(0,len(s)-1)