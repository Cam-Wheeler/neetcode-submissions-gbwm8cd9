class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        cache = {}
        for idx in range(len(nums)):
            difference = target - nums[idx]
            if difference in cache:
                return [cache[difference], idx]
            cache[nums[idx]] = idx
