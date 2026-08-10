class Solution:
    def evenOddBit(self, n: int) -> List[int]:
        binary=bin(n)
        binary=binary.lstrip('0b')[::-1]
        result=[0,0]
        for i in range(len(binary)):
            if binary[i]=='1':
                if i%2==0:
                    result[0]+=1
                else:
                    result[1]+=1
        return result
        