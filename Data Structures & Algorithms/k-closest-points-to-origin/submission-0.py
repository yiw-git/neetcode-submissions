class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distances=[]
        for i in range(len(points)):
            dist=points[i][0]**2+points[i][1]**2
            distances.append([dist, points[i][0], points[i][1]])
        
        heapq.heapify(distances)

        output=[]
        while k>0:
            d1=heapq.heappop(distances)
            output.append([d1[1],d1[2]])
            k-=1

        return output


