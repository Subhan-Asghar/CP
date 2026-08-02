class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        if poured==0:
            return 0.000
        result=[[poured]]
        for i in range(1,query_row+1):
            ans=[0]*(i+1)
            for j in range(i+1):
                if j==0 or j==i:
                    if result[-1][-1]>1:
                        ans[j]+=(result[-1][-1]-1)/2
                    continue
                if result[-1][j-1]>1:
                    ans[j]+=(result[-1][j-1]-1)/2
                if result[-1][j]>1:
                    ans[j]+=(result[-1][j]-1)/2
            result.append(ans)
        ans=result[query_row][query_glass]
        if ans>=1:
            return 1
        return ans