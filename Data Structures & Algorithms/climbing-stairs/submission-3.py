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
                n1 = recurse(n - 1)
                n2 = recurse(n - 2)
                memo[n] = n1 + n2
                return memo[n]
        
        result = recurse(n)
        print(memo)
        return result