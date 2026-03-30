class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)

        output = []
        for idx in range(len(nums) - 2):
            target = -(nums[idx])
            head = idx + 1
            tail = len(nums) - 1
            if idx > 0 and nums[idx] == nums[idx - 1]: # Catches deduplication in the outer loop
                continue
            while head < tail:
                partial_sum = nums[head] + nums[tail]
                if partial_sum > target:
                    tail -= 1
                elif partial_sum < target:
                    head += 1
                else:
                    # It hits our target. 
                    output.append([nums[idx], nums[head], nums[tail]])
                    head += 1

                    # Deduplication
                    while nums[head] == nums[head - 1] and head < tail:
                        head += 1
            
        return output

        

