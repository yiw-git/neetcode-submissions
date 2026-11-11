class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones=[-x for x in stones]
        heapq.heapify(stones)

        while len(stones)>1:
            biggest=heapq.heappop(stones)
            bigger=heapq.heappop(stones)
            if biggest<bigger:
                #biggest=-8, bigger=-5
                new_stone=biggest-bigger
                heapq.heappush(stones, new_stone)
        if not stones:
            return 0
        output=-stones[0]
        return output
            

