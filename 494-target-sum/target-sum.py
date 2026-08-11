class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n=len(nums)
        memo={}
        def solve(index,amount):
            if index==n:
                if amount==target:
                    return 1
                return 0
            if (index,amount) in memo:
                return memo[(index,amount)]
            neg=solve(index+1,amount-nums[index])
            pos=solve(index+1,amount+nums[index])
            ans=neg+pos
            memo[(index,amount)]=ans
            return ans
        return solve(0,0)