class Solution:
    def countPairs(self, words: List[str]) -> int:
        count=0
        n=len(words)
        m=len(words[0])
        hashmap={}
        for index,word in enumerate(words):
            s=[0]*(m-1)
            for j in range(1,m):
                s[j-1]=(ord(word[j-1])-ord(word[j]))%26
            tuple_s=tuple(s)
            if tuple_s not in hashmap:
                hashmap[tuple_s]=1
            else:
                hashmap[tuple_s]+=1
        for key in hashmap:
            c=hashmap[key]
            count+=(c*(c-1))//2
        return count       
