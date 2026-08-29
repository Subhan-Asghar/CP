from collections import Counter
class Solution:
    def minDeletions(self, s: str) -> int:
        count=Counter(s)
        count = sorted([list(x) for x in count.items()],key=lambda x:x[1],reverse=True)
        ans=0
        sett=set()
        for _,freq in count:
            while freq in sett and freq>0:
                freq-=1
                ans+=1
            sett.add(freq)
        return ans
