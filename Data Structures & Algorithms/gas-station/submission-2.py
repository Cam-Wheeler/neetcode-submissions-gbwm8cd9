class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1
        
        def drive(start):
            current_gas = 0
            idx = start
            for _ in range(len(gas)):
                current_gas += gas[idx]
                if current_gas <= 0 or current_gas < cost[idx]:
                    return False

                # Make the trip.
                current_gas -= cost[idx]
                idx += 1
                if idx == len(gas):
                    idx = 0

                if idx == start:
                    return True

        for idx in range(len(gas)):
            if drive(idx):
                return idx
        
        return -1

            


