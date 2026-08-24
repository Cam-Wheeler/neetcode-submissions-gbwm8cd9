class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        used = [False] * len(nums)
        max_depth = len(nums)
        res = []

        def dfs(depth, current):

            if depth == len(nums):
                res.append(current.copy())
                return
            
            for idx in range(len(nums)):
                if not used[idx]:
                    used[idx] = True
                    current.append(nums[idx])
                    dfs(depth + 1, current)
                    current.pop()
                    used[idx] = False
            
            return

        dfs(0, [])

        return res