class Solution:
    def rob(self, nums: List[int]) -> int:
        n=len(nums)
        if n==1:
            return nums[0]
        memo={}
        def solve(index,n):
            if index>=n:
                return 0
            if (index,n) in memo:
                return memo[(index,n)]
            take=nums[index]+solve(index+2,n)
            not_take=solve(index+1,n)
            ans=max(take,not_take)
            memo[(index,n)]=ans
            return ans
        return max(solve(0,n-1),solve(1,n))