import heapq as hq
class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        events=[]
        for cap,start,end in trips:
            hq.heappush(events,(start,cap))
            hq.heappush(events,(end,-cap))
        count=0
        while events:
            _,cap=hq.heappop(events)
            count+=cap
            if count>capacity:
                return False
        return True
        