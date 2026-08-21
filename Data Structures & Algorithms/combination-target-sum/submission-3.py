class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        max_idx = len(nums)
        res = []
        def dfs(idx, curr, curr_sum):

            if curr_sum == target:
                res.append(curr.copy())
                return
            
            if idx >= max_idx or curr_sum > target:
                return

            # Include the current element
            val = nums[idx]
            curr.append(val)
            dfs(idx, curr, curr_sum + val)

            # move onto the next element
            curr.pop()
            dfs(idx + 1, curr, curr_sum)

            return

        dfs(0, [], 0)

        return res

            