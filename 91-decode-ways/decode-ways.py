class Solution:
    def numDecodings(self, s: str) -> int:
        n=len(s)
        memo={}
        def solve(index):
            if index>n:
                return 0
            if index==n:
                return 1
            if s[index]=="0":
                return 0
            if index in memo:
                return memo[index]
            ans=solve(index+1)
            if index+1<n and 10<=int(s[index:index+2])<=26:
                ans+=solve(index+2)
            memo[index]=ans
            return ans
        return solve(0)