class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        events=[]
        for cap,start,end in trips:
            events.append((start,cap))
            events.append((end,-cap))
        events.sort()
        count=0
        for _,cap in events:
            count+=cap
            if count>capacity:
                return False
        return True
        