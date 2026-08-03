class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort() # O(n log n)

        res = []
        idx = 0
        while idx < len(nums) - 2:
            l, r = idx + 1, len(nums) - 1
            while l < r:
                three_sum = nums[idx] + nums[l] + nums[r]
                if three_sum == 0:
                    res.append([nums[idx], nums[l], nums[r]])
                if three_sum < 0:
                    l += 1
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
                else:
                    r -= 1
                    while r > l and nums[r] == nums[r + 1]:
                        r -= 1
            idx += 1
            while idx < len(nums) and nums[idx] == nums[idx - 1]:
                idx += 1
        return res