class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        n=len(s)
        high=0
        low=0
        count=0
        ans=""
        for high in range(n):
            if s[high]=="1":
                count+=1

            while count==k:
                while low<=high and s[low]=="0":
                    low+=1
                
                curr=s[low:high+1]
                if ans=="" or len(curr)<len(ans) or (len(curr)==len(ans) and curr<ans):
                    ans=curr
                
                count-=1
                low+=1
        return ans
                


       