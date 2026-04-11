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

    private int count = 0, result = 0;
    private boolean found = false;

    public int kthSmallest(TreeNode root, int k) {

        this.dfs(root, k);
        return this.result;
    }

    public void dfs(TreeNode node, int k) {

        if(node == null || found) {return;}

        this.dfs(node.left, k);

        this.count++;
        if(this.count == k) {
            this.result = node.val;
            this.found = true;
            return;
        }

        this.dfs(node.right, k);
    }
}
