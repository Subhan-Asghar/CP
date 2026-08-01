class Solution:
    def partition(self, s: str) -> List[List[str]]:
        n=len(s)
        def pali(val):
            l=0
            h=len(val)-1
            while l<h:
                if val[l]!=val[h]:
                    return False
                l+=1
                h-=1
            return True

        def solve(index,path):
            if path and not pali(path[-1]):
                return 
            if len("".join(path))==n:
                result.append(path[:])
                return 
            prev=""
            for i in range(index,n):
                prev+=s[i]
                path.append(prev)
                solve(i+1,path)
                path.pop()
        result=[]
        solve(0,[])
        return result
        
            