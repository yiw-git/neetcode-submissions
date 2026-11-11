
from collections import Counter, deque
import heapq

class Solution:
    def leastInterval(self, tasks: list[str], n: int) -> int:
        freq = Counter(tasks)

        # Max heap: negative frequencies
        max_heap = [-count for count in freq.values()]
        heapq.heapify(max_heap)

        # Queue: [remaining_frequency, release_time]
        cooldown = deque()

        time = 0

        while max_heap or cooldown:

            # Advance one CPU cycle
            time += 1

            # Release ALL tasks whose cooldown has finished
            while cooldown and cooldown[0][1] <= time:
                remaining, release_time = cooldown.popleft()
                heapq.heappush(max_heap, remaining)

            # Execute one available task
            if max_heap:
                remaining = heapq.heappop(max_heap)
                remaining += 1

                if remaining < 0:
                    cooldown.append([remaining, time + n + 1])

        return time
