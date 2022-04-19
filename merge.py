"""
You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n,
representing the number of elements in nums1 and nums2 respectively.

Merge nums1 and nums2 into a single array sorted in non-decreasing order.


"""





class Solution:
    from typing import List

    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if n == 0:
            return
        if m == 0:
            nums1[0:] = nums2
            return
        j = n - 1
        ins = len(nums1) - 1
        i = m - 1
        while True:
            if i >= 0:
                if nums1[i] < nums2[j]:
                    nums1[ins] = nums2[j]
                    j -= 1
                    ins -= 1
                else:
                    nums1[ins] = nums1[i]
                    i -= 1
                    ins -= 1
            else:
                nums1[ins] = nums2[j]
                j -= 1
                ins -= 1
            if j < 0:
                break





a = [4, 0, 0, 0]
b = [1, 2, 3]
Solution().merge(a, 1, b, 3)
print(a)
