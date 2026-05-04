class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def dfs(idx, sublist, current_total):

            if idx == len(nums) or current_total >= target:
                if current_total == target:
                    res.append(sublist.copy())
                return
            
            sublist.append(nums[idx])
            dfs(idx, sublist, current_total + nums[idx])
            sublist.pop()
            dfs(idx + 1, sublist, current_total)
            return
        
        dfs(0, [], 0)
        return res
