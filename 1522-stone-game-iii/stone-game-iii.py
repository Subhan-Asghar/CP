class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        memo={}
        def solve(index):
            if index==n: return 0

            if index in memo:
                return memo[index]
            first=stoneValue[index]-solve(index+1)
            second=float("-inf")
            third=float("-inf")

            if index+1<n:
                second=(stoneValue[index]+stoneValue[index+1])-solve(index+2)
            if index+2<n:
                third=(stoneValue[index]+stoneValue[index+2]+stoneValue[index+1])-solve(index+3)
           
            ans=max(first,second,third)
            memo[index]=ans
            return ans
        n=len(stoneValue)
        ans=solve(0)
        if ans<0:return "Bob"
        if ans>0:return "Alice"
        if ans==0:return "Tie"