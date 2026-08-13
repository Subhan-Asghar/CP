class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        n=len(days)
        memo={}
        def solve(index):
            if index==n:
                return 0
            if index in memo:
                return memo[index]

            day=costs[0]+solve(index+1)   
            week_val=days[index]+6

            week=costs[1]
            month=costs[2]
            for i in range(index,n):
                if days[i]>week_val:
                    week=week+solve(i)
                    break
            month_val=days[index]+29
            for j in range(index,n):
                if days[j]>month_val:
                    month=month+solve(j)
                    break
            ans=min(day,week,month)
            memo[index]=ans
            return ans
        return solve(0)
          