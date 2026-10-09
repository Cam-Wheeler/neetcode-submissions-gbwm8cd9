class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        num_len = len(nums)
        k = k % num_len

        if k != 0:

            nums.reverse()

            # first k
            l, r = 0, k - 1
            while l < r:
                tmp = nums[r]
                nums[r] = nums[l]
                nums[l] = tmp
                l += 1
                r -= 1
            
            # rest
            l, r = k, num_len - 1
            while l < r:
                tmp = nums[r]
                nums[r] = nums[l]
                nums[l] = tmp
                l += 1
                r -= 1

            
            
            
            


    