class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
        max_product = float("-inf")

        for i in range(len(nums)):
            sub_product = nums[i]
            for j in range(i, len(nums)):
                if i == j:
                    multiply = 1
                else:
                    multiply = nums[j]

                sub_product = sub_product * multiply
                max_product = max(max_product, sub_product)
            
        return max_product

                