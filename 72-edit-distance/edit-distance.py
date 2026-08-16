class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        def solve(m,n):
            if m==0:
                return n 
            if n==0:
                return m
            if (m,n) in memo:
                return memo[(m,n)]

            if word1[m-1]==word2[n-1]:
                ans=solve(m-1,n-1)
            else:
                ans=1+min(solve(m-1,n),solve(m,n-1),solve(m-1,n-1))
            memo[(m,n)]=ans
            return ans
        memo={}
        return solve(len(word1),len(word2))