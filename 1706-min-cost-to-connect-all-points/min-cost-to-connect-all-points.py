import heapq as hq
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        qr,qc=points[0]
        heap=[(0,qr,qc)]
        visited=set()
        cost=0
        while heap:
            w,qr,qc=hq.heappop(heap)
            if (qr,qc) in visited:
                continue
            visited.add((qr,qc))
            cost+=w
            for u,v in points:
                if (u,v) not in visited:
                    val=abs(qr-u) +abs(qc-v)
                    hq.heappush(heap,(val,u,v))
        return cost