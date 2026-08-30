class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        
        hashmap={}
        for i,n in enumerate(nums):
            hashmap[n]=i
        n=len(nums)
        high=hashmap[max(nums)]
        low=hashmap[min(nums)]

        # Distance from the one end
        start=max(high,low)+1
        end=n-min(high,low) # 8 -1

        # Distance remove from the start and end 
        s=min(high,low)+1
        e=n-max(high,low)
     
        return min(start,end,s+e)






