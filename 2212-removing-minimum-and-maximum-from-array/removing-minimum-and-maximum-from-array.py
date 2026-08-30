class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        n=len(nums)
        high=nums.index(max(nums))
        low=nums.index(min(nums))
        
        max_ele=max(high,low)
        min_ele=min(high,low)
        # Distance from the one end
        start=max_ele+1
        end=n-min_ele

        # Distance remove from the start and end 
        s=min_ele+1
        e=n-max_ele
     
        return min(start,end,s+e)






