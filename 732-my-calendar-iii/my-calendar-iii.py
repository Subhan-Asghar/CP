class MyCalendarThree:

    def __init__(self):
        
        self.events=[]
    def book(self, startTime: int, endTime: int) -> int:
        self.events.append((startTime,1))
        self.events.append((endTime,-1))

        self.events.sort()
        count=0
        booking=0
        for _, changes in self.events:
            count+=changes
            booking=max(booking,count)
        return booking


# Your MyCalendarThree object will be instantiated and called as such:
# obj = MyCalendarThree()
# param_1 = obj.book(startTime,endTime)