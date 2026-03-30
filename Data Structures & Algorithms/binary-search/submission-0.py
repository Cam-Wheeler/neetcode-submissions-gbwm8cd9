class Solution:
    def search(self, nums: List[int], target: int) -> int:
        head = 0
        tail = len(nums) - 1

        while head <= tail:
            middle = (head + tail) // 2
            if nums[middle] == target:
                return middle
            elif nums[middle] > target:
                tail = middle - 1
            else:
                head = middle + 1
        return -1 