class Solution:
    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        # arr=[0]*(days+2)
        # for u,v in meetings:
        #     arr[u]+=1
        #     arr[v+1]-=1

        # ans=0
        # start=0
        # for i in range(1,len(arr)-1):
        #     start+=arr[i]
        #     if start==0:
        #         ans+=1
        # return ans
        last=0
        meetings.sort()
        ans=0
        for index,(u,v) in enumerate(meetings):
            if last<u:
                ans+=u-last-1
            last=max(last,v)
            ans

        ans += days - last
        return ans

