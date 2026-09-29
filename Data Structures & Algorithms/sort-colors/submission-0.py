class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        flag = True
        while flag:
            swap = 0
            for idx in range(0, len(nums) - 1):
                if nums[idx] > nums[idx + 1]:
                    tmp = nums[idx + 1]
                    nums[idx + 1] = nums[idx]
                    nums[idx] = tmp
                    swap += 1
            if swap == 0:
                flag = False