class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        subarray = nums[0]
        result = nums[0]

        for num in nums[1:]:
            subarray = max(num, subarray + num)
            result = max(result, subarray)
        return result
