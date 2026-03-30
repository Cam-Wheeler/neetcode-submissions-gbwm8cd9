class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if len(nums) == 1:
            if nums[0] == target:
                return 0
            else:
                return -1
        
        head = 0
        tail = len(nums) - 1
        middle = (head + tail) // 2

        while nums[tail] < nums[middle]:
            head = middle + 1
            middle = (head + tail) // 2
        
        while nums[head] > nums[middle]:
            head += 1
        
        # Now head is pointing at the inflection point. 

        h1 = head
        t1 = tail
        if target >= nums[head] and target <= nums[tail]:
            bs_head = h1
            bs_tail = t1
        else:
            bs_head = 0
            bs_tail = h1 - 1

        print(bs_head, bs_tail)
        
        # Now we do binary search. 
        while bs_head <= bs_tail:
            middle = (bs_head + bs_tail) // 2
            if nums[middle] == target:
                return middle
            elif nums[middle] > target:
                bs_tail = middle - 1
            else:
                bs_head = middle + 1
        
        return -1
                
            