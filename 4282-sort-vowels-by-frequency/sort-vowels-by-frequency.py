from collections import defaultdict
from functools import cmp_to_key
class Solution:
    def sortVowels(self, s: str) -> str:
        hashmap=defaultdict(int)
        location={}
        index=0
        for i in s:
            if i in "aeiou":
                hashmap[i]+=1
                if i not in location:
                    location[i]=index
                    index+=1
        items=hashmap.items()
        if not items:
            return s
        def vowels_comp(item1,item2):
            ele1,count1=item1
            ele2,count2=item2

            if count1!=count2:
                return count1-count2
            return location[ele2]-location[ele1]

  
        
        vowels = sorted(items, key=cmp_to_key(vowels_comp))
        print(vowels)
        ele,count=vowels.pop()
        s=list(s)
        for i in range(len(s)):
            if s[i] in "aeiou":
                if count==0:
                    ele,count=vowels.pop()
                s[i]=ele
                count-=1
        return "".join(s)
