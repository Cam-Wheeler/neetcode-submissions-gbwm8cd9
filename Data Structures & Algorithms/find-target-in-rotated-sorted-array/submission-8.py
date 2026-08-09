class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l < r:
            m = (l + r) // 2
            if nums[m] < nums[r]:
                r = m
            else:
                l = m + 1

        pivot = l
        if target < nums[pivot]:
            return -1
        
        l, r = 0, len(nums) - 1
        if target >= nums[pivot] and target <= nums[r]:
            l, r = pivot, r
        else:
            l, r = 0, pivot - 1
        
        while l <= r:
            m = (l + r) // 2
            if nums[m] == target:
                return m
            elif nums[m] > target:
                r = m - 1
            else:
                l = m + 1
        
        return -1