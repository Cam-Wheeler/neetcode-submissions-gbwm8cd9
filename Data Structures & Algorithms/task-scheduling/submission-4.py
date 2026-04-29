from collections import Counter, deque
import heapq

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:

        counts = Counter(tasks)
        heap = []
        for task, count in counts.items():
            heapq.heappush_max(heap, (count, task))

        queue = deque()
        current_time = 0
        while heap or queue:

            if queue and queue[0][-1] == current_time:
                heapq.heappush_max(heap, queue.popleft()[0])
            
            if heap:
                node = heapq.heappop_max(heap)
                node = (node[0] - 1, node[1]) # Decrement the count
                if node[0] > 0:
                    queue.append((node, current_time + n + 1))
            
            current_time += 1
        
        return current_time




