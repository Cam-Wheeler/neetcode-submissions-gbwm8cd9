class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        
        def dfs(idx, sublist):

            if idx == len(nums):
                result.append(sublist.copy())
                return
            sublist.append(nums[idx])
            dfs(idx + 1, sublist)
            sublist.pop()
            dfs(idx + 1, sublist)
            return

        dfs(0, [])
        return result