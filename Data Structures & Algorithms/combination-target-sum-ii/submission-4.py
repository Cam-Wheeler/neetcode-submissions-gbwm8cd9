class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []

        def dfs(idx, subarray, total):

            if total == target:
                result.append(subarray.copy())
                return 

            if idx >= len(candidates) or total > target:
                return

            subarray.append(candidates[idx])
            dfs(idx + 1, subarray, total + candidates[idx])
            subarray.pop()
            while idx + 1 < len(candidates) and candidates[idx] == candidates[idx + 1]:
                idx += 1
            dfs(idx + 1, subarray, total)
        
        
        candidates.sort()
        dfs(0, [], 0)
        return result