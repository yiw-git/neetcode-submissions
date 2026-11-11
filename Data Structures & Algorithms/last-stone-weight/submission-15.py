import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones=[-s for s in stones]
        heapq.heapify(stones)

        while len(stones)>=2:
            s1=heapq.heappop(stones)
            s2=heapq.heappop(stones)

            
            if s2>s1:
                s2=-abs(s2-s1)
                heapq.heappush(stones,s2)
            #s1==s2, then stones is []
        return abs(stones[0]) if stones else 0
            