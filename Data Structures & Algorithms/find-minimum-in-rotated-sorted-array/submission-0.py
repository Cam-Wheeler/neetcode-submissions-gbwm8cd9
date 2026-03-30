class Solution:
    def findMin(self, nums: List[int]) -> int:
        res = nums[0]
        head, tail = 0, len(nums) - 1

        while head <= tail:
            if nums[head] < nums[tail]:
                res = min(res, nums[head])
                break
            middle = (head + tail) // 2
            res = min(res, nums[middle])

            if nums[middle] >= nums[head]:
                head = middle + 1
            else:
                tail = middle - 1
        return res