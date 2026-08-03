class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort() # O(n log n)

        res = []
        idx = 0
        while idx < len(nums) - 2:
            
            if idx > 0 and nums[idx] == nums[idx - 1]:
                idx += 1
                continue

            l, r = idx + 1, len(nums) - 1
            while l < r:
                three_sum = nums[idx] + nums[l] + nums[r]
                if three_sum < 0:
                    l += 1
                elif three_sum > 0:
                    r -= 1
                else:
                    res.append([nums[idx], nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1
            idx += 1
        return res