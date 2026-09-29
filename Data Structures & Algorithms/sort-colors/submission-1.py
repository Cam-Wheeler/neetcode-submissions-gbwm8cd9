class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        buckets = [0, 0, 0]
        for i in nums:
            buckets[i] += 1

        idx = 0
        for bucket_idx in range(3):
            for count in range(buckets[bucket_idx]):
                nums[idx] = bucket_idx
                idx += 1
        