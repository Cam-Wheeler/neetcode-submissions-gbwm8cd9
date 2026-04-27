from math import ceil
from collections import deque
class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        ttt = [(pos, (target - pos) / speed) for pos, speed in zip(position, speed)]
        ttt.sort()
        ttt = deque(ttt)
        print(ttt)
        fleets = 1
        pos, time_to_arrival = ttt.pop()
        while ttt:
            if time_to_arrival < ttt[-1][1]:
                fleets += 1
                pos, time_to_arrival = ttt.pop()
            else:
                ttt.pop()
        
        return fleets



