class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        if len(nums) == 0:
            return 0
    
        head = 0
        tail = len(nums) - 1

        while head <= tail:
            if nums[head] == val:
                nums[head] = nums[tail]
                tail -= 1
            else:
                head += 1
        
        return head
            
        

        

        