class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def backtrack(current, open_b, close_b):
            
            # Final
            if len(current) == n * 2:
                if open_b == close_b:
                    res.append(current)
                return 

            if close_b > open_b:
                return
            
            current += "("
            backtrack(current, open_b + 1, close_b)
            current = current[:-1]
            current += ")"
            backtrack(current, open_b, close_b + 1)

            return

        


        backtrack("", 0, 0)

        return res