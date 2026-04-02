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

            double aLeft = (i > 0) ? A[i-1] : Double.NEGATIVE_INFINITY;
            double aRight = (i < A.length) ? A[i] : Double.POSITIVE_INFINITY;
            double bLeft = (j > 0) ? B[j-1] : Double.NEGATIVE_INFINITY;
            double bRight = (j < B.length) ? B[j] : Double.POSITIVE_INFINITY; 

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
