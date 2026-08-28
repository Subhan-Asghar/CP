class Solution:
    def minimumPushes(self, word: str) -> int:
        count=[0]*26
        for i in word:
            count[ord(i)-97]+=1
        count.sort(reverse=True)
        mul=1
        rep=1
        ans=0
        for num in count:
            if num==0:
                break
            if rep>8:
                mul+=1
                rep=1
            ans+=mul*num
            rep+=1
        return ans