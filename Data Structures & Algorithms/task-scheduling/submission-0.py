class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count=Counter(tasks) #[1,3,0,0,4]
        maxHeap=[-cnt for cnt in count.values()] #[-1,-3,0,0,-4]
        heapq.heapify(maxHeap) #[-4,0,0,-3,-1]want to process the most frequent first
        
        time=0
        q=deque()
        #while the heap is not empty or the cooldown queue is not empty
        while maxHeap or q:
            time+=1
            if not maxHeap:
                time=q[0][1]
            else:
                cnt=1+heapq.heappop(maxHeap)
                if cnt:
                    q.append([cnt, time+n])
            if q and q[0][1]==time:
                heapq.heappush(maxHeap, q.popleft()[0])
        return time

            


