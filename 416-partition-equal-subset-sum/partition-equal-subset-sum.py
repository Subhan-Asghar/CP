class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total_sum=sum(nums)
        if total_sum%2!=0:
            return False
        target=total_sum//2
        n=len(nums)
        memo={}
        def solve(index,amount):
            if amount==target:
                return True
            if  amount>target or index==n:
                return False
            if (index,amount) in memo:
                return memo[(index,amount)]
            if solve(index+1,amount+nums[index]):
                return True
            if solve(index+1,amount):
                return True
            memo[(index,amount)]=False
            return False
        return solve(0,0)