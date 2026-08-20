class Solution:
    def profitableSchemes(self, n: int, minProfit: int, group: List[int], profit: List[int]) -> int:
        memo={}
        MOD=(10**9)+7
        def solve(index,amount,members):
       
            if index==len(group):
                if amount>=minProfit:
                    return 1
                return 0
            take=0
            state=(index,amount,members)
            if state in memo:
                return memo[state]
            if members+group[index]<=n:
                new_amount = min(minProfit, amount + profit[index])
                take=solve(index+1,new_amount,members+group[index])           
            skip=solve(index+1,amount,members)
            ans=(take+skip)%MOD
            memo[state]=ans
            return ans
       
        return solve(0,0,0)