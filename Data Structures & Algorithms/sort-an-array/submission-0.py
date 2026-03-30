class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        if len(nums) <= 1:
            return nums
        
        mid = len(nums) // 2
        left = nums[:mid]
        right = nums[mid:]
        left_result = self.sortArray(left)
        right_result = self.sortArray(right)

        merged = self.merge(left_result, right_result)

        return merged
    
    def merge(self, left: List[int], right: List[int]) -> List[int]:

        merged = []
        i = j = 0

        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                merged.append(left[i])
                i += 1
            else:
                merged.append(right[j])
                j += 1
        
        merged.extend(left[i:])
        merged.extend(right[j:])

        return merged
