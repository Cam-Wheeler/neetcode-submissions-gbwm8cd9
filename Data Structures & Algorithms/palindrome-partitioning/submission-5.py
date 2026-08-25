class Solution:
    def partition(self, s: str) -> List[List[str]]:
        
        res = []
        current = []

        def dfs(l, r):

            # base case
            if r >= len(s):
                if l == len(s):
                    res.append(current.copy())
                return

            # split
            if self.is_palindrome(s, l, r):
                current.append(s[l: r + 1])
                dfs(r + 1, r + 1)
                current.pop()

            # no split
            dfs(l, r + 1)

            return 
        
        dfs(0, 0)
        return res


    def is_palindrome(self, s, l, r):
        while l <= r:
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1
        return True