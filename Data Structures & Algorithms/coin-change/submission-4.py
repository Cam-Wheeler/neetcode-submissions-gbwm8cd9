class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        if amount == 0:
            return 0

        memo = {}

        def recurse(amount):

            if amount == 0:
                return 0
            
            if amount in memo:
                return memo[amount]

            result = float("inf")
            for coin in coins:
                if amount - coin >= 0:
                    result = min(result, 1 + recurse(amount - coin))
            
            memo[amount] = result

            return result
        
        minCoin = recurse(amount)

        return -1 if minCoin == float("inf") else minCoin



            
            



            