class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        memo={0:cost[0],
        1:cost[1]
        }
        n=len(cost)
        def solve(n):
            if n in memo:
                return memo[n]
            ans=min(solve(n-1),solve(n-2))+cost[n]
            memo[n]=ans
            return ans
        return min(solve(n-1),solve(n-2))