class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        cache = {}

        for idx in range(len(nums)):
            diff = target - nums[idx]
            if diff in cache:
                return [cache[diff], idx]
            cache[nums[idx]] = idx
        
