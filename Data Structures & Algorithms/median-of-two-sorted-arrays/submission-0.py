class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        arr = sorted(nums1 + nums2)

        left = 0
        right = len(arr) - 1

        while left <= right:
            mid = (left + right) // 2

            if len(arr) % 2 > 0:
                return arr[mid]
            else:
                return (arr[mid] + arr[mid + 1]) / 2

        