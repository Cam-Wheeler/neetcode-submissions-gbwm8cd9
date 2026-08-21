class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        max_depth = len(nums)
        res = []
        def dfs(current, idx):
            if idx == max_depth:
                res.append(current.copy())
                return
            
            # Include the element
            current.append(nums[idx])
            dfs(current, idx + 1)
            
            # Skip the element
            current.pop()
            dfs(current, idx + 1)

            return

        dfs([], 0)
        return res