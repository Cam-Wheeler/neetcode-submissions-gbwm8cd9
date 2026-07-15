class Solution:
    def change(self, amount: int, coins: List[int]) -> int:

        memo = {}
        coins.sort()

        def dfs(idx, total):

            if idx == len(coins) and total != amount:
                return 0

            if total == amount:
                return 1

            if total > amount:
                return 0

            if (idx, total) in memo:
                return memo[(idx, total)]

            memo[(idx, total)] = dfs(idx, total + coins[idx]) + dfs(idx + 1, total)

            return memo[(idx, total)]

        return dfs(0,0)


            