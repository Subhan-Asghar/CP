class Solution:
    def numsSameConsecDiff(self, n: int, k: int) -> List[int]:
        result=[]
        def solve(m,path):
            if m==n:
                print(path)
                result.append(int("".join(path)))
                return 
            for i in range(0,10):
                if i==0 and m==0:
                    continue
                if path:
                    if abs(int(path[-1])-i)==k:
                        path.append(f"{i}")
                    else:
                        continue
                else:
                    path.append(f"{i}")
                solve(m+1,path)
                path.pop()
        solve(0,[])
        return result
                
