class Solution:
    def minHeightShelves(self, books: List[List[int]], shelfWidth: int) -> int:
        def solve(index):
            if index==n:
                return 0
            if index in memo:
                return memo[index]
            curr_w=shelfWidth
            height=0
            res=float("inf")
            for i in range(index,n):
                w,h=books[i]
                if curr_w<w:
                    break
                curr_w-=w
                height=max(height,h)
                res=min(res,solve(i+1)+height)
            memo[index]=res
            return res
        memo={}
        n=len(books)
        return solve(0)