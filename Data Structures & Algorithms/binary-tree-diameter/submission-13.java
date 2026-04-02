/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */

class Solution {
    int diameter = 0;
    public int diameterOfBinaryTree(TreeNode root) {
        this.maxDepth(root);
        return diameter;
    }

    public int maxDepth(TreeNode root) {
        if(root == null) {return 0;}

        int maxL = this.maxDepth(root.left), maxR = this.maxDepth(root.right);
        diameter = Integer.max(this.diameter, maxL+maxR);

        return 1 + Integer.max(maxL, maxR);
    }
}
