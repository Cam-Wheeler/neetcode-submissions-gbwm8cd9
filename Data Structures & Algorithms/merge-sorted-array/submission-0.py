class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        m_idx = m
        for num in nums2:
            nums1[m_idx] = num
            m_idx += 1

        nums1.sort() 