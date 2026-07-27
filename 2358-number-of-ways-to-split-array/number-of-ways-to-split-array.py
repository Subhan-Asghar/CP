class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        totalsum=sum(nums)
        presum=0
        n=len(nums)
        split=0
        for i in range(n-1):
            totalsum-=nums[i]
            presum+=nums[i]
            if presum>=totalsum:
                split+=1
        return split