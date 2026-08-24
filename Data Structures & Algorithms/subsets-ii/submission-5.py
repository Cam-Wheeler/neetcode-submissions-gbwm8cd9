class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:

        nums.sort() # O(n log n)
        max_idx = len(nums)
        current = []
        res = []

        def dfs(idx):

            if idx == max_idx:
                res.append(current.copy())
                return

            # happy route
            current.append(nums[idx])
            dfs(idx + 1)
            current.pop()

            # sad route (skip duplicates)
            while idx + 1 < len(nums) and nums[idx] == nums[idx + 1]:
                idx += 1 # skipping dupes
            idx += 1 # the correct place
            dfs(idx)

            return

        dfs(0)

        return res
            