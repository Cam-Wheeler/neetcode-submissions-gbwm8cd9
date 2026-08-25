class Solution:
    def letterCombinations(self, digits: str) -> List[str]:

        if digits == "":
            return []

        num_char_map = {
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

        def dfs(idx, current):

            if idx == len(digits):
                res.append("".join(current))
                return
            
            num = digits[idx]
            for char in num_char_map[num]:
                current.append(char)
                dfs(idx + 1, current)
                current.pop()

            return

        dfs(0, [])

        return res
