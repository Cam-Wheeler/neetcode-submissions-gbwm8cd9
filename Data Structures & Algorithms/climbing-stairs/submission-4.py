class Solution:
    def climbStairs(self, n: int) -> int:
        
        memo = {}

        def recurse(n):

            if n < 0:
                return 0
            if n == 0:
                return 1
            elif n in memo:
                return memo[n]
            else:
                memo[n] = recurse(n - 1) + recurse(n - 2)
                return memo[n]
    
        return recurse(n)