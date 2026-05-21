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

    private int preIndex = 0, inIndex = 0;

    public TreeNode buildTree(int[] preorder, int[] inorder) {
        return dfs(Integer.MAX_VALUE, preorder, inorder);
    }

    private TreeNode dfs(int limit, int[] preorder, int[] inorder) {
        if(preIndex >= preorder.length) {return null;}
        if(inorder[inIndex] == limit) {
            inIndex++;
            return null;
        }

        TreeNode root = new TreeNode(preorder[preIndex]);
        preIndex++;
        root.left = dfs(root.val, preorder, inorder);
        root.right = dfs(limit, preorder, inorder);
        return root;
    }
}
