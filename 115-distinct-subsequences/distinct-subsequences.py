class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        memo={}
        def solve(m,n,text):
            if text==t:
                return 1
            if m==0 or n==0:
                return 0
            if (m,n,text) in memo:
                return memo[(m,n,text)]
            ans=0
            if s[m-1]==t[n-1]:
                ans+=solve(m-1,n-1,t[n-1]+text)
                ans+=solve(m-1,n,text)
            else:
                ans+=solve(m-1,n,text)
            memo[(m,n,text)]=ans
            return ans
        return solve(len(s),len(t),"")
        