import heapq
from collections import deque, Counter

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:

        task_count = Counter(tasks)
        max_heap = []

        for val, count in task_count.items():
            heapq.heappush_max(max_heap, (count, val))

        q = deque() # (cycle the task becomes available again, num of this task, task)

        curr_cycle = 0
        while max_heap or q:

            if q and q[0][0] == curr_cycle:
                _, task_num, task = q.popleft()
                heapq.heappush_max(max_heap, (task_num, task))

            if max_heap:
                task_num, task = heapq.heappop_max(max_heap)
                task_num -= 1
                if task_num > 0:
                    can_use_again = curr_cycle + n + 1
                    q.append((can_use_again, task_num, task))
            
            curr_cycle += 1
        

        return curr_cycle