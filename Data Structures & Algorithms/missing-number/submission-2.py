class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        res = 0

        nums.sort()

        for idx in range(len(nums)):
            if nums[idx] != idx + 1:
                res = idx + 1
        return res