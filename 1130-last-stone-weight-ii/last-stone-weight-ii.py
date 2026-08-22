class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        total=sum(stones)
        target=total//2
        memo={}
        n=len(stones)
        
        def solve(amount,index):
            if amount>=target or index==n:
                return abs(amount-(total-amount))
            if (amount,index) in memo:
                return memo[(amount,index)]
       
            take=solve(amount+stones[index],index+1)
            skip=solve(amount,index+1)
            ans=min(take,skip)
            memo[(amount,index)]=ans
            return ans
        return solve(0,0)