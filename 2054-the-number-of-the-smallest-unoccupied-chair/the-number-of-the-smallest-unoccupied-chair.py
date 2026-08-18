class Solution:
    def smallestChair(self, times: List[List[int]], targetFriend: int) -> int:
        n=len(times)
        event=[]
        arive=[0]*n # zero means free and 1 means taken
        for i,(u,v) in enumerate(times):
            event.append((u,1,i))
            event.append((v,0,i))
        event.sort()
        hashmap={}
        for _,_,index in event:
            if index not in hashmap:
                for chair in range(n):
                    if arive[chair]==0:
                        if index== targetFriend:
                            return chair
                        arive[chair]=1
                        hashmap[index]=chair
                        break
            # if already in the hashmap then it means time is the leave time 
            else:
                arive[hashmap[index]]=0
                del hashmap[index]
                


                    