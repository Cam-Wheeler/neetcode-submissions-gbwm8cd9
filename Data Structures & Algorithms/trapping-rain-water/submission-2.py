class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        res = 0
        l_max = 0
        r_max = 0
        while l < r:
            l_max = max(l_max, height[l])
            r_max = max(r_max, height[r])
            if height[l] < height[r]:
                l += 1
                if min(l_max, r_max) - height[l] > 0:
                    res += min(l_max, r_max) - height[l]
            else:
                r -= 1
                if min(l_max, r_max) - height[r] > 0:
                    res += min(l_max, r_max) - height[r]
        return res
                
