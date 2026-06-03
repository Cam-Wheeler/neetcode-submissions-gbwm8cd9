class Solution:
    def canJump(self, nums: List[int]) -> bool:
        goal = len(nums) - 1
        for idx in range(len(nums) - 2, -1, -1):
            if nums[idx] >= goal - idx:
                goal = idx
        
        return True if goal == 0 else False