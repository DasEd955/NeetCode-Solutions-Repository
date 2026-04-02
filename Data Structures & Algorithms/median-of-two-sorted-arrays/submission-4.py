class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:

        combinedNums = nums1 + nums2
        combinedNums.sort()
        left, right = 0, len(combinedNums) - 1

        while left < right:
            middle = left + (right - left) // 2
            if len(combinedNums) % 2 != 0:
                return combinedNums[middle]
            else:
                left = middle + 1
                right = middle
        
        return (combinedNums[left] + combinedNums[right]) / 2.0
        