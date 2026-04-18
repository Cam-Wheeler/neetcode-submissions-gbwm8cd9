class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def dfs(i: int, current: list, total: int) -> None:

            if total == target:
                res.append(current.copy())
                return
            if i >= len(nums) or total > target:
                return
            
            current.append(nums[i])
            dfs(i, current, total + nums[i])
            current.pop()
            dfs(i + 1, current, total)

        dfs(0, [], 0)
        return res
