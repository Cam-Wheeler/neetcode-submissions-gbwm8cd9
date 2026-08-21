class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:

        candidates.sort()
        res = []
        max_idx = len(candidates)
    
        def dfs(idx, curr, curr_sum):

            if curr_sum == target:
                res.append(curr.copy())
                return 

            if idx >= max_idx or curr_sum > target:
                return

            # include it
            val = candidates[idx]
            curr.append(val)
            dfs(idx + 1, curr, curr_sum + val)

            # skip it
            curr.pop()
            idx += 1
            while idx < max_idx and candidates[idx] == candidates[idx - 1]:
                idx += 1
            dfs(idx, curr, curr_sum)

            return

        dfs(0, [], 0)

        return res