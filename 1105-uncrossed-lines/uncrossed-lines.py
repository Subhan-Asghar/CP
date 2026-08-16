class Solution:
    def maxUncrossedLines(self, nums1: List[int], nums2: List[int]) -> int:
        def solve(m,n):
            if m==0 or n==0:
                return 0
            if (m,n) in memo:
                return memo[(m,n)]
            if nums1[m-1]==nums2[n-1]:
                ans=1+solve(m-1,n-1)
            else:
                ans=max(solve(m-1,n),solve(m,n-1))
            memo[(m,n)]=ans
            return ans
        memo={}
        return solve(len(nums1),len(nums2))