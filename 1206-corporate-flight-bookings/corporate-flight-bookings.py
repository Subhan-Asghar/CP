class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        result=[0]*(n+1)
        for first,last,seats in bookings:
            result[first-1]+=seats
            result[last]-=seats
        prefix=0
        for i,num in enumerate(result):
            result[i]+=prefix
            prefix+=num
        return result[:n]
