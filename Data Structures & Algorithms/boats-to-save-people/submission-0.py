class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()

        l, r = 0, len(people) - 1
        boats = 0

        while l <= r:
            pair_weight = people[l] + people[r]
            if pair_weight > limit:
                r -= 1
                boats += 1
            else:
                r -= 1
                l += 1
                boats += 1
        return boats