class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []

        def dfs(idx, current, total):
            if total == target:
                result.append(current.copy())
                return
            if idx >= len(nums) or total > target:
                return
            
            current.append(nums[idx])
            dfs(idx, current, total + nums[idx])
            current.pop()
            dfs(idx + 1, current, total)
        
        dfs(0, [], 0)
        return result