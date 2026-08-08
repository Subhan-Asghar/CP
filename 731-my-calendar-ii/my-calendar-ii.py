import heapq as hq 
class MyCalendarTwo:

    def __init__(self):
        self.events=[]

    def book(self, startTime: int, endTime: int) -> bool:
        if not self.events:
            hq.heappush(self.events,(startTime,1))
            hq.heappush(self.events,(endTime,-1))
            return True
        temp_heap=self.events[:]
        count=0
        hq.heappush(temp_heap,(startTime,1))
        hq.heappush(temp_heap,(endTime,-1))
        while temp_heap:
            book,changes=hq.heappop(temp_heap)
            count+=changes
            if count>=3:
                return False
                
        hq.heappush(self.events,(startTime,1))
        hq.heappush(self.events,(endTime,-1))
        return True


# Your MyCalendarTwo object will be instantiated and called as such:
# obj = MyCalendarTwo()
# param_1 = obj.book(startTime,endTime)