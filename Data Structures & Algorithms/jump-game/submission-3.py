class Solution:
    def canJump(self, nums: List[int]) -> bool:
        goal = len(nums) - 1
        for idx in range(len(nums) - 2, -1, -1):
            if nums[idx] >= goal - idx:
                goal = idx
            else:
                continue
        
        return goal == 0