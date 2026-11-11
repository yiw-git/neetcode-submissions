import heapq
from collections import deque
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count=Counter(tasks) #[1,3,0,0,4]
        maxHeap=[-cnt for cnt in count.values()] #[-1,-3,0,0,-4]
        heapq.heapify(maxHeap) #[-4,0,0,-3,-1]want to process the most frequent first
        cooldown=deque()
        time=0

        while cooldown or maxHeap:
            time+=1
            if cooldown and cooldown[0][1]<=time:
                remaining, available_time=cooldown.popleft()
                heapq.heappush(maxHeap,remaining)

            if maxHeap:
                remaining=heapq.heappop(maxHeap)

                remaining+=1
                if remaining<0:
                    cooldown.append([remaining, time+1+n])

        return time



            


