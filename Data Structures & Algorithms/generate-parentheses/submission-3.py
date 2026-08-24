class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        o_cnt = 1
        c_cnt = 0
        current = "("
        res = []

        def dfs(current, o_cnt, c_cnt):

            if o_cnt > n:
                return

            if c_cnt > o_cnt:
                return
            
            if o_cnt == c_cnt and o_cnt == n and c_cnt == n:
                res.append(current)
            
            current_o = current + "("
            dfs(current_o, o_cnt + 1, c_cnt)

            current_c = current + ")"
            dfs(current_c, o_cnt, c_cnt + 1)

            return

        dfs(current, o_cnt, c_cnt)
        return res

