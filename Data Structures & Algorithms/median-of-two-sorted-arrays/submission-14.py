class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:

        A, B = nums1, nums2
        total = len(A) + len(B)
        half = total // 2

        if len(A) > len(B):
            A, B = B, A
        
        left, right = 0, len(A) - 1

        while True:
            i = left + (right - left) // 2
            j = half - i - 2

            aLeft, aRight = A[i] if i >= 0 else float("-inf"), A[i+1] if i+1 < len(A) else float("inf")
            bLeft, bRight = B[j] if j >= 0 else float("-inf"), B[j+1] if j+1 < len(B) else float("inf")

            if aLeft <= bRight and bLeft <= aRight:
                if total % 2:
                    return min(aRight, bRight)
                return (max(aLeft, bLeft) + min(aRight, bRight)) / 2
            elif aLeft > bRight:
                right = i - 1
            else:
                left = i + 1