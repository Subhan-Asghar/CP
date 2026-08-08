class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        if not firstList or not secondList:
            return []
        pointA=0
        pointB=0
        result=[]
        while pointA<len(firstList) and pointB<len(secondList):
            first=firstList[pointA]
            second=secondList[pointB]
            if first[0]<=second[1] and second[0]<=first[1]:
                ans=[max(first[0],second[0]),min(first[1],second[1])]
                result.append(ans)
            if second[1]>=first[1]:
                pointA+=1
            else:
                pointB+=1

        return result
                