class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        merged = [0] * (m + n)
        i, j = 0, 0
        idx = 0
        while i < m and j < n:
            if nums1[i] < nums2[j]:
                merged[idx] = nums1[i]
                i += 1
                idx += 1
            else:
                merged[idx] = nums2[j]
                j += 1
                idx += 1

        while i < m:
            merged[idx] = nums1[i]
            i += 1
            idx += 1

        while j < n:
            merged[idx] = nums2[j]
            j += 1
            idx += 1
        
        for idx in range(len(merged)):
            nums1[idx] = merged[idx]

