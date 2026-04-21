class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()

        for idx, val in enumerate(nums):
            
            if val > 0: # We cannot get 0 with all positive nums
                break
            
            if idx > 0 and val == nums[idx - 1]: # We have a duplicate value, lets skip.
                continue
            
            l = idx + 1
            r = len(nums) - 1
            while l < r:
                three_sum = val + nums[l] + nums[r]
                if three_sum < 0:
                    l += 1
                elif three_sum > 0:
                    r -= 1
                else:
                    result.append([val, nums[l], nums[r]])
                    l += 1
                    while nums[l] == nums[l - 1] and l < r: 
                        l += 1

        return result