from collections import Counter, deque
import heapq

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counts = Counter(tasks)
        max_heap = [cnt for cnt in counts.values()]
        heapq.heapify_max(max_heap)
        q = deque()

        time = 0
        while max_heap or q:
            time += 1

            if max_heap:
                node = heapq.heappop_max(max_heap) - 1
                if node > 0:
                    q.append((node, time + n))
            
            if q and q[0][1] == time:
                node = q.popleft()
                heapq.heappush_max(max_heap, node[0])
        
        return time

