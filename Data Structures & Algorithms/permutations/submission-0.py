class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        picked = [False] * len(nums)

        def dfs(current, nums, picked):

            if len(current) == len(nums):
                result.append(current.copy())
                return

            for i in range(len(nums)):
                if not picked[i]:
                    current.append(nums[i])
                    picked[i] = True
                    dfs(current, nums, picked)
                    current.pop()
                    picked[i] = False
        
        dfs([], nums, picked)
        return result