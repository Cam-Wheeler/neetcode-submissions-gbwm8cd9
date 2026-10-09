class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        num_len = len(nums)

        if k != 0:
            new_array = [0] * num_len

            for idx in range(len(nums)):
                new_idx = idx + k
                while new_idx >= num_len - 1:
                    new_idx -= num_len
                new_array[new_idx] = nums[idx]

            for idx in range(len(new_array)):
                nums[idx] = new_array[idx]

    