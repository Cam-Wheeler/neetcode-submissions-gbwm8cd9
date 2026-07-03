class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        stack = []

        def backtrack(open_b, closed_b):

            if open_b == closed_b and len(stack) == 2*n:
                res.append("".join(stack))
                return

            if open_b < n:
                stack.append("(")
                backtrack(open_b + 1, closed_b)
                stack.pop()

            if closed_b < open_b:
                stack.append(")")
                backtrack(open_b, closed_b + 1)
                stack.pop()

            return

        backtrack(0, 0)

        return res