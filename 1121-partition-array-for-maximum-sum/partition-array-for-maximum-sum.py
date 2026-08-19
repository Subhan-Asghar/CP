class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        memo={}
        def solve(index):
            if index==n:
                return 0
            if index in memo:
                return memo[index]
            max_ele=0
            res=0
            for i in range(index,min(n,index+k)):
                max_ele=max(max_ele,arr[i])
                window=(i-index)+1
                res=max(res,solve(i+1)+(max_ele*window))
            memo[index]=res
            return res
        n=len(arr)
        return solve(0)