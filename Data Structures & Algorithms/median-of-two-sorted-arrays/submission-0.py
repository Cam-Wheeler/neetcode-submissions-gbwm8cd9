class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        res = []

        num1 = 0
        num2 = 0

        while num1 < len(nums1) and num2 < len(nums2):
            if nums1[num1] < nums2[num2]:
                res.append(nums1[num1])
                num1 += 1
            else:
                res.append(nums2[num2])
                num2 += 1
        
        if num1 == len(nums1):
            res.extend(nums2[num2:])
        else:
            res.extend(nums1[num1:])

        
        print(res)

        if len(res) % 2 == 0:
            return (res[len(res) // 2] + res[(len(res) // 2) - 1]) / 2
        else:
            return res[len(res) // 2]