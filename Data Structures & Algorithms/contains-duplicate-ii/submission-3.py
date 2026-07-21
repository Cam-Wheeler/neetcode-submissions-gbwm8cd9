class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        
        seen = set()

        for idx, val in enumerate(nums):

            if val in seen:
                return True
            seen.add(val)
            if len(seen) > k:
                seen.remove(nums[idx - k])

        return False


