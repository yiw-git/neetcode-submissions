class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums_neg=[-x for x in nums]
        heapq.heapify(nums_neg)

        while k>0:
            val=heapq.heappop(nums_neg)
            k-=1
        return -1*val


