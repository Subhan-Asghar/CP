class Solution:
    def hammingWeight(self, n: int) -> int:
        res=bin(n).lstrip("0b")
        count=0
        for i in res:
            if i=="1":
                count+=1
        return count