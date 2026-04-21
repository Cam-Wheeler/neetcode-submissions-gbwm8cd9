from math import ceil

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        if len(piles) == h:
            return max(piles)
        
        # We need to search for the result
        left = 1
        right = max(piles)
        best_eating_speed = 1
        while left <= right:
            middle = (left + right) // 2
            time = 0
            for pile in piles:
                time += ceil(pile / middle)
            if time <= h:
                right = middle - 1
                best_eating_speed = middle
            else:
                left = middle + 1

        return best_eating_speed