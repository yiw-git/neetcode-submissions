import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        dist=[]
        res=[]
        
        for point in points:
            dis=math.sqrt(point[0]**2+point[1]**2)
            dist.append((dis,point))
        heapq.heapify(dist)
        while k>0:
            a=heapq.heappop(dist)
            res.append(a[1])
            k-=1


        return res

