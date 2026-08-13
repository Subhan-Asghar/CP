class Solution:
    def rob(self, nums: List[int]) -> int:
        n=len(nums)
        memo={}
        def solve(index):
            if index>=n:
                return 0
            if index in memo:
                return memo[index]
            take=nums[index]+solve(index+2)
            skip=solve(index+1)
            ans=max(take,skip)
            memo[index]=ans
            return ans
        return solve(0)
