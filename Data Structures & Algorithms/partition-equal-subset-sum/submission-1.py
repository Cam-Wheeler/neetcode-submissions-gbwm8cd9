class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2 == 1:
            return False


        half = int(total / 2)
        memo = {}

        def dfs(idx, current):

            if idx == len(nums):
                return current == half

            if (idx, current) in memo:
                return memo[(idx, current)]

            include = dfs(idx + 1, current + nums[idx])
            exclude = dfs(idx + 1, current)
            memo[(idx, current)] = include or exclude

            return memo[(idx, current)]
        
        return dfs(0, 0)


            

              