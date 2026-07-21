class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        
        memo = {}

        m, n = len(word1), len(word2)

        def dfs(i, j):

            if i == len(word1) and j == len(word2):
                return 0

            if i == m:
                return n - j

            if j == n:
                return m - i

            if (i, j) in memo:
                return memo[(i, j)]

            res = 0
            if word1[i] == word2[j]:
                res += dfs(i + 1, j + 1)
            elif word1[i] != word2[j]:
                res = min(1 + dfs(i, j + 1), 1 + dfs(i + 1, j + 1)) # smallest of future add and replace
                res = min(res, 1 + dfs(i + 1, j)) # smallest of future add, replace and delete
            memo[(i, j)] = res
            return res

        return dfs(0, 0)