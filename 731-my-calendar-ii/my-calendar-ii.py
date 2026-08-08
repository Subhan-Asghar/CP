import heapq as hq 
class MyCalendarTwo:

    def __init__(self):
        self.events=[]

    def book(self, startTime: int, endTime: int) -> bool:
        if not self.events:
            self.events.append((startTime,1))
            self.events.append((endTime,-1))
            return True
        temp_heap=self.events[:]
        count=0
        temp_heap.append((startTime,1))
        temp_heap.append((endTime,-1))
        temp_heap.sort()
        for _ , changes in temp_heap:
            count+=changes
            if count>=3:
                return False

        self.events=temp_heap[:]
        return True


# Your MyCalendarTwo object will be instantiated and called as such:
# obj = MyCalendarTwo()
# param_1 = obj.book(startTime,endTime)