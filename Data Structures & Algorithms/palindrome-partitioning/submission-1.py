class Solution:
    def partition(self, s: str) -> List[List[str]]:

        res = []

        def dfs(current, i):

            if i >= len(s):
                res.append(current.copy())
                return
            
            for j in range(i, len(s), 1):
                if self.is_palindrome(s, i, j):
                    current.append(s[i:j+1])
                    dfs(current, j + 1)
                    current.pop()
            return

        dfs([], 0)

        return res

    def is_palindrome(self, s, l, r):
        
        while l <= r:
            if s[l] == s[r]:
                l += 1
                r -= 1
            else:
                return False
        return True