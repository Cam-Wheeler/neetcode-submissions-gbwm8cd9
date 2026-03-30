class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        if len(nums) == 0:
            return 0
        
        k = 0
        head = 0
        tail = len(nums) - 1

        while head <= tail:

            if head == tail and nums[head] != val:
                return k + 1
            elif head == tail and nums[head] == val:
                return k

            if nums[head] == val:
                while nums[tail] == val:
                    tail -= 1
                    if tail == head:
                        return k
                tmp = nums[head]
                nums[head] = nums[tail]
                nums[tail] = tmp
            k += 1
            head += 1
        return k
        

        

        