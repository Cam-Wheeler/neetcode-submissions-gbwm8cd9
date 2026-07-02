class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []

        def dfs(current, i):

            if i == len(nums):
                res.append(current.copy())
                return
            
            current.append(nums[i])
            dfs(current, i + 1)
            current.pop()

            while i + 1 < len(nums) and nums[i] == nums[i + 1]:
                i += 1
            
            dfs(current, i + 1)

            return

        nums.sort()
        dfs([], 0)

        return res



