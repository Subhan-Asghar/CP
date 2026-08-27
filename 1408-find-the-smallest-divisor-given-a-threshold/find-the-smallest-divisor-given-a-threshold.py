import math
class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        low=1
        high=max(nums)
        while low<high:
            mid=(low+high)//2
           
            total=sum([math.ceil(x/mid) for x in nums ])
            if total>threshold:
                low=mid+1
            else:
                high=mid
        return high