class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        
        cache = set()
        cache.add(0)
        ptr = 0

        for num in nums:
            if num > 0:
                cache.add(num)
                while ptr + 1 in cache:
                    ptr += 1
        
        return ptr + 1