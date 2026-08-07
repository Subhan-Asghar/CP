class MyCalendar:

    def __init__(self):
        
        self.event=[]

    def book(self, startTime: int, endTime: int) -> bool:
        if not self.event:
            self.event.append([startTime,endTime])
            return True
        for i in range(len(self.event)):
            last=self.event[i]
            if last[0]<endTime and startTime<last[1]:
                return False
        self.event.append([startTime,endTime])
        return True


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(startTime,endTime)