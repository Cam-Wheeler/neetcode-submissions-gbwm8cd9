class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
        result = []
        candidates.sort()

        def dfs(idx, sub_array, total):
            if total == target:
                result.append(sub_array.copy())
                return
            if idx >= len(candidates) or total > target:
                return
            
            sub_array.append(candidates[idx])
            dfs(idx + 1, sub_array, total + candidates[idx])
            sub_array.pop()
            while idx + 1 < len(candidates) and candidates[idx] == candidates[idx + 1]:
                idx += 1
            dfs(idx + 1, sub_array, total)

        dfs(0, [], 0)
        return result