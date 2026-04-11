from math import ceil

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left, right = 1, max(piles)
        current_best = right

        while left <= right:
            middle = (left + right) // 2
            total_hours = 0
            for pile in piles:
                total_hours += math.ceil(pile / middle)
            
            if total_hours <= h:
                current_best = middle
                right = middle - 1
            else:
                left = middle + 1
        return current_best