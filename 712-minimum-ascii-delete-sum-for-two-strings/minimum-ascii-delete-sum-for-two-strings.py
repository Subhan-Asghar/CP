class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        val1=sum(map(ord,s1))
        val2=sum(map(ord,s2))
        memo={}
        def solve(m,n):
            if m==0 or n==0:
                return 0
            if (m,n) in memo:
                return memo[(m,n)]
            if s1[m-1]==s2[n-1]:
                ans=ord(s1[m-1])+solve(m-1,n-1)
            else:
                ans=max(solve(m-1,n),solve(m,n-1))
            memo[(m,n)]=ans
            return ans
        ans=solve(len(s1),len(s2))
        result=(val1-ans)+(val2-ans)
        return result