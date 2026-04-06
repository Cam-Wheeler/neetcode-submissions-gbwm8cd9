class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        val_set = set()
        for i in nums:
            if i in val_set:
                return i
            val_set.add(i)
        
            