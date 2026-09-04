class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        count=0
        while True:
            p=pow(2,count)
            if p==n:
                return True
            elif p>n:
                return False
            count+=1
        