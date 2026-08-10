class Solution:
    def addBinary(self, a: str, b: str) -> str:
        ans=""
        a=int(a)
        b=int(b)
        if not a and not b :
            return "0"
        carry=0
        while a or b:
            lasta=a%10
            lastb=b%10
            a=a//10
            b=b//10
            sum_ele=lasta+lastb+carry
            carry=sum_ele//2
            sum_ele=sum_ele%2
            ans=f"{sum_ele}"+ans
        if carry:
            return str(carry)+ans
        return ans
            


