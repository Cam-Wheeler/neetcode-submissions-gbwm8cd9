class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def backtrack(current, open_b, closed_b):

            if open_b == closed_b and len(current) == 2*n:
                res.append(current)
                return

            if open_b < n:
                current += "("
                backtrack(current, open_b + 1, closed_b)
                current = current[:-1]

            if closed_b < open_b:
                current += ")"
                backtrack(current, open_b, closed_b + 1)
                current = current[:-1]

            return

        backtrack("", 0, 0)

        return res