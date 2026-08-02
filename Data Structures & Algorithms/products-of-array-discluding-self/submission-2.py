class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        forward = [0] * len(nums)
        forward[0] = 1
        backward = [0] * len(nums)
        backward[-1] = 1

        for idx in range(1, len(nums)):
            multi = nums[idx - 1] * forward[idx - 1]
            forward[idx] = multi
        
        for idx in range(len(nums) - 2, -1, -1):
            multi = nums[idx + 1] * backward[idx + 1]
            backward[idx] = multi

        res = []
        for fwd, bwd in zip(forward, backward):
            res.append(fwd * bwd)
        return res
