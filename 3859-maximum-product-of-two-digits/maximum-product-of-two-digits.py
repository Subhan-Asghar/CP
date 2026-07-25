import heapq as hq
class Solution:
    def maxProduct(self, n: int) -> int:
        heap=[]
        while n!=0:
            val=n%10
            hq.heappush(heap,-val)
            n=n//10
        ele1=-hq.heappop(heap)
        ele2=-hq.heappop(heap)
        return ele1*ele2 