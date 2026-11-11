import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        #nums=[-s for s in nums]
        
        heap=[]
        
        for num in nums:
            heapq.heappush(heap, num)
            if len(heap)>k:
                heapq.heappop(heap)


        return heap[0]


        

