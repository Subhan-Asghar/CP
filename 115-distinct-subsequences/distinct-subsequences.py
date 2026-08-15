class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        memo={}
        def solve(m,n):
            if n==0:
                return 1
            if m==0:
                return 0
            if (m,n) in memo:
                return memo[(m,n)]
            ans=0
            if s[m-1]==t[n-1]:
                ans+=solve(m-1,n-1)
                ans+=solve(m-1,n)
            else:
                ans+=solve(m-1,n)
            memo[(m,n)]=ans
            return ans
        return solve(len(s),len(t))
        