class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = [1] * len(nums)
        product = 1
        for i in range(1, len(nums), 1):
            product = product * nums[i - 1]
            output[i] = product
        
        product = 1
        for i in range(len(nums) - 2, -1, -1):
            product = product * nums[i + 1]
            output[i] = output[i] * product
        
        return output