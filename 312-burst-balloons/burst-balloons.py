class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        nums=[1]+nums+[1]
        def solve(i,j):
            if i>j:
                return 0
            if (i,j) in memo:
                return memo[(i,j)]
            ans=0
            for k in range(i,j+1):
                left=solve(i,k-1)
                right=solve(k+1,j)
                cost=left+right+(nums[i-1]*nums[k]* nums[j+1])
                ans=max(ans,cost)
            memo[(i,j)]=ans
            return ans
        n=len(nums)
        memo={}
        return solve(1,n-2)