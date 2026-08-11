class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # n=len(nums)
        # memo={}
        # def solve(index,prev):
        #     if index==n:
        #         return 0
        #     if (index,prev) in memo:
        #         return memo[(index,prev)]
        #     not_take=solve(index+1,prev)
        #     take=0
        #     if prev==-1 or nums[index]>nums[prev]:
        #         take=1+solve(index+1,index)
        #     ans=max(take,not_take)
        #     memo[(index,prev)]=ans
        #     return ans
        # return solve(0,-1)
        dp = [1] * len(nums)
        for i in range(1, len(nums)):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)

        return max(dp)