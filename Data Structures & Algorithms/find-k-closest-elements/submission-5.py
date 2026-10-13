class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        if k == len(arr):
            return arr

        l = 0
        end = len(arr)
        for r in range(len(arr)):
            is_closer = abs(arr[r] - x)
            if r >= k:
                if is_closer < abs(arr[l] - x):
                    l += 1
                # We are less than x still so we need to continue searching
                elif (is_closer == abs(arr[l] - x)) and (arr[r] < x):
                    l += 1
                else: # we are passed x so if its not smaller we can return
                    return arr[l:r]
        
        return arr[l:]
            