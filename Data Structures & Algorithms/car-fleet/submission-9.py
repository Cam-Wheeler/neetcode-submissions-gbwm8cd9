from collections import deque

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        pos_speed = []
        for idx in range(len(position)):
            pos_speed.append((position[idx], speed[idx]))

        pos_speed.sort(key=lambda x: x[0])

        stack = deque()

        for idx in range(len(pos_speed)):
            pos, speed = pos_speed[idx]
            time = (target - pos) / speed
            stack.append((time))

        fleets = 0
        while stack:
            current_time = stack.pop()
            fleets += 1
            while stack and stack[-1] <= current_time:
                stack.pop()

        return fleets