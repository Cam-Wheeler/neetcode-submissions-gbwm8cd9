class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []

        def dfs(current, i):

            if i == len(nums):
                if current not in res:
                    res.append(current.copy())
                return 
            
            current.append(nums[i])
            dfs(current, i + 1)
            current.pop()
            dfs(current, i + 1)

            return

        nums.sort()
        dfs([], 0)

        return res



