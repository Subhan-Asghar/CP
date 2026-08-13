class Solution:
    def tribonacci(self, n: int) -> int:
        memo={
            0:0,
            1:1,
            2:1,
        }
        def solve(n):
            if n in memo:
                return memo[n]
            ans=solve(n-1)+solve(n-2)+solve(n-3)
            memo[n]=ans
            return ans
        return solve(n)