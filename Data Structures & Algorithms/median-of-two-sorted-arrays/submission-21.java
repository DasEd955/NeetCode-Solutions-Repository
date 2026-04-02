class Solution {
    public double findMedianSortedArrays(int[] nums1, int[] nums2) {
        
        int[] A = nums1, B = nums2;
        int total = A.length + B.length;
        int half = (int)total / 2;

        if(A.length > B.length) {
            int[] temp = A;
            A = B;
            B = temp;
        }

        int left = -1, right = A.length - 1;

        while(true) {
            int i = left + (right - left) / 2;
            int j = half - i - 2;
            double aLeft = (i >= 0) ? A[i] : Double.NEGATIVE_INFINITY;
            double aRight = (i < A.length - 1) ? A[i+1] : Double.POSITIVE_INFINITY;
            double bLeft = (j >= 0) ? B[j] : Double.NEGATIVE_INFINITY;
            double bRight = (j < B.length - 1) ? B[j+1] : Double.POSITIVE_INFINITY;

            if(aLeft <= bRight && bLeft <= aRight) {
                if(total % 2 != 0) {
                    return Double.min(aRight, bRight);
                }
                else {
                    return (Double.max(aLeft, bLeft) + Double.min(aRight, bRight)) / 2;
                }
            }
            else if(aLeft > bRight) {
                right = i - 1;
            }
            else {
                left = i + 1;
            }
        }

    }
}
