class Solution:
    def mctFromLeafValues(self, arr: List[int]) -> int:
        def solve(i,j):
            if i==j:
                return 0
            if (i,j) in memo:
                return memo[(i,j)]
            ans=float("inf")
            for k in range(i,j):
                max_left=max(arr[i:k+1])
                max_right=max(arr[k+1:j+1])
                left=solve(i,k)
                right=solve(k+1,j)
                curr=left+right+max_left*max_right
                ans=min(ans,curr)
            memo[(i,j)]=ans
            return ans
        memo={}
        n=len(arr)
        return solve(0,n-1)
        