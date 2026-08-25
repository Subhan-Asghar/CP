class Solution:
    def countSubstrings(self, s: str) -> int:
        n=len(s)
        def pali(l,r):
            count=0
            while l>=0 and r<n and s[l]==s[r]: 
                count+=1
                l-=1
                r+=1
            return count

        count=0
        for i in range(n):
            count+=1
            count+=pali(i-1,i+1)
            count+=pali(i,i+1)
        return count