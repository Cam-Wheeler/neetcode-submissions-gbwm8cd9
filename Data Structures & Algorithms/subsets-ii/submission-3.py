class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        cache = set()

        def dfs(current, i):

            if i == len(nums):
                if tuple(current) not in cache:
                    cache.add(tuple(current))
                return
            
            current.append(nums[i])
            dfs(current, i + 1)
            current.pop()
            dfs(current, i + 1)

            return

        nums.sort()
        dfs([], 0)

        return [list(group) for group in cache]



