class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:

        memo = {}
        
        def dfs(i, j, k):

            if i == len(s1) and j == len(s2) and k == len(s3):
                return True
            
            if k == len(s3) and (i != len(s1) or j != len(s2)):
                return False

            if (i, j) in memo:
                return memo[(i, j)]

            res = False
            if i < len(s1) and s1[i] == s3[k]:
                res = dfs(i + 1, j, k + 1)
            if not res and j < len(s2) and s2[j] == s3[k]:
                res = dfs(i, j + 1, k + 1)
            
            memo[(i, j)] = res

            return res

        if s1 == "" or s2 == "":
            return s1 == s3 or s2 == s3
            
        return dfs(0, 0, 0)