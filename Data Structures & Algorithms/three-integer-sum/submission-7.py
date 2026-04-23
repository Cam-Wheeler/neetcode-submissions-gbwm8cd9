class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        for idx, val in enumerate(nums):

            if val > 0:
                break
            
            if idx > 0 and val == nums[idx - 1]:
                continue
            
            left = idx + 1
            right = len(nums) - 1
            while left < right:
                threeSum = val + nums[left] + nums[right]
                if threeSum > 0:
                    right -= 1
                elif threeSum < 0:
                    left += 1
                else:
                    res.append([val, nums[left], nums[right]])
                    left += 1
                    right -= 1
                    while nums[left] == nums[left - 1] and left < right:
                        left += 1
            
        return res
            
            
        
