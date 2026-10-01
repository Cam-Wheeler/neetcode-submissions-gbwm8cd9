class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        memo = {}

        def recurse(idx, holding):

            if idx == len(prices):
                return 0

            if (idx, holding) in memo:
                return memo[(idx, holding)]
            
            res = recurse(idx + 1, holding)
            if holding: # sell
                res = max(res, prices[idx] + recurse(idx + 1, False))
            else: # buy
                res = max(res, -prices[idx] + recurse(idx + 1, True))
            memo[(idx, holding)] = res
            return res

        return recurse(0, False)