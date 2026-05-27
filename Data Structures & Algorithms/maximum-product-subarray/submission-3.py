class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
        result, curr_max, curr_min = nums[0], nums[0], nums[0]

        for num in nums[1:]:
            tmp = curr_max * num # needed for current min calculation, as we overwrite current max first! 
            curr_max = max(curr_max * num, curr_min * num, num)
            curr_min = min(tmp, curr_min * num, num)
            result = max(result, curr_max)
        
        return result