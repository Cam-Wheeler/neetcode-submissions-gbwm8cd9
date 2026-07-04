from collections import defaultdict

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:

        if digits == "":
            return []

        mappings = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }


        res = []

        def dfs(current, idx):

            if idx == len(digits):
                res.append(current)
                return

            chars = mappings[digits[idx]]
            for char in chars:
                current += char
                dfs(current, idx + 1)
                current = current[:-1]
            return

        dfs("", 0)
        return res


