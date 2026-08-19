class Solution:
    def largestSumOfAverages(self, nums: List[int], k: int) -> float:
        n=len(nums)
        prefix=[0]*n
        prefix[0]=nums[0]
        for i in range(1,n):
            prefix[i]=prefix[i-1]+nums[i]
        memo={}
        def solve(index,k):
            
            if k==0:
                return 0 if index==n else float('-inf')
            if index==n:
                return float("-inf")
            
            if (index,k) in memo:
                return memo[(index,k)]
            ans=0
            for i in range(index, n-k+ 1):
                window=(i-index)+1
                if index==0:
                    val=prefix[i]/window
                else:
                    val=(prefix[i]-prefix[index-1])/window
                
                ans=max(ans,solve(i+1,k-1)+val)
            memo[(index,k)]=ans
            return ans
        return solve(0,k)
                

                