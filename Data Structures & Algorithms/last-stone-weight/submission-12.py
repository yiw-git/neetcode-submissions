class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones=[-s for s in stones]
        heapq.heapify(stones)
        
        while len(stones)>=2: #if len is odd, then only one element raise error

            heavy1=heapq.heappop(stones)
            heavy2=heapq.heappop(stones)
            if heavy2>heavy1:
                heapq.heappush(stones, heavy1-heavy2)
           
            #print(new_s)
        stones.append(0)    
        #stones=[-s for s in stones]
        return abs(stones[0])

