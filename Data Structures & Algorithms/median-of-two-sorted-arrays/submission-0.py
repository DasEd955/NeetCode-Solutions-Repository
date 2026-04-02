import statistics

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:

        combinedNums = nums1 + nums2
        left, right = 0, len(combinedNums) - 1
        median = statistics.median(combinedNums)
        return median

        #while left <= right:
            #middle = left + (right - left) // 2:
            #if nums[middle] 
        