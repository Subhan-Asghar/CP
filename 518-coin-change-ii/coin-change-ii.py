class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        n=len(coins)
        memo={}
        def knapsack(amount,index):
            if amount==0:
                return 1
            if index==n:
                return 0
            if (amount,index) in memo:
                return memo[(amount,index)]
            if coins[index]>amount:
                ans=knapsack(amount,index+1)
            else:
                take=knapsack(amount-coins[index],index)
                not_take=knapsack(amount,index+1)
                ans=take+not_take
            memo[(amount,index)]=ans
            return ans
            
        return knapsack(amount,0)