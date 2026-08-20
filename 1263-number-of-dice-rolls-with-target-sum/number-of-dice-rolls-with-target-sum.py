class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        memo={}
        def knapsack(n,amount):
            if amount==0 and n==0:
                return 1
            if amount<0 or n==0:
                return 0
            if (n,amount) in memo:
                return memo[(n,amount)]
            ans=0
            for i in range(1,k+1):
                ans+=knapsack(n-1,amount-i)
            memo[(n,amount)]=ans
            return ans
        return knapsack(n,target)%((10**9) +7 )