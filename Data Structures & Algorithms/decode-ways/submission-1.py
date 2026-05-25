class Solution:
    def numDecodings(self, s: str) -> int:
        memo = {len(s): 1}

        def recurse(idx):

            if idx == len(s):
                return 1
            if idx in memo:
                return memo[idx]
            if s[idx] == "0":
                return 0

            res = recurse(idx + 1)
            if idx < len(s) - 1 and (s[idx] == "1" or s[idx] == "2" and s[idx + 1] in "0123456"):
                res += recurse(idx + 2)
            memo[idx] = res
            return res

        return recurse(0)
