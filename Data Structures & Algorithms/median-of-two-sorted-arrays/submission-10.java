class Solution {
    public double findMedianSortedArrays(int[] nums1, int[] nums2) {
        
        int[] A = nums1, B = nums2;
        int total = A.length + B.length;
        int half = (int)(total / 2);

        if(A.length > B.length) {
            int[] temp = A;
            A = B;
            B = temp;
        }

        int left = 0, right = A.length;

        while(true) {

            int i = left + (right - left) / 2;
            int j = half - i;

            double aLeft, aRight, bLeft, bRight;

            if(i > 0) {
                aLeft = A[i-1];
            }
            else {
                aLeft = Double.NEGATIVE_INFINITY;
            }

            if(i < A.length) {
                aRight = A[i];
            }
            else {
                aRight = Double.POSITIVE_INFINITY;
            }

            if(j > 0) {
                bLeft = B[j-1];
            }
            else {
                bLeft = Double.NEGATIVE_INFINITY;
            }

            if(j < B.length) {
                bRight = B[j];
            }
            else {
                bRight = Double.POSITIVE_INFINITY;
            }

            if(aLeft <= bRight && bLeft <= aRight) {

                if(total % 2 != 0) {
                    return Double.min(aRight, bRight);
                }

                return (Double.max(aLeft, bLeft) + Double.min(aRight, bRight)) / 2;
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
