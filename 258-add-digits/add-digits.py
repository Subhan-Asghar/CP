class Solution:
    def addDigits(self, num: int) -> int:
        s=str(num)
        while len(s)>1:
            ans=0
            for i in s:
                ans+=int(i)
            s=str(ans)
        return int(s)