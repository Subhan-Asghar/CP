class Solution:
    def grayCode(self, n: int) -> List[int]:
        n=(2**n)
        result=[]
        for i in range(n):
            result.append(i^(i>>1))
        return result