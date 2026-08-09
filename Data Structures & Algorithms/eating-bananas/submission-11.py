class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        max_piles = max(piles)
        current_min = max_piles

        l, r = 1, max_piles
        while l <= r:
            middle = (l + r) // 2
            total_time = 0
            for pile in piles:
                total_time += math.ceil(pile / middle)
            if total_time <= h:
                current_min = min(current_min, middle)
                r = middle - 1
            else:
                l = middle + 1

        return current_min