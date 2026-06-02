class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:

        memo = {}

        def recurse(i, j):

            if i == len(text1) or j == len(text2):
                return 0

            if (i, j) in memo:
                return memo[(i, j)]
            
            if text1[i] == text2[j]:
                memo[(i, j)] = 1 + recurse(i + 1, j + 1)
            else:
                memo[(i, j)] = max(recurse(i + 1, j), recurse(i, j + 1))
            
            return memo[(i, j)]
        
        return recurse(0, 0)

    