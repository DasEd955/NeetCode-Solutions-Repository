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

    private ArrayList<Integer> result = new ArrayList<>();

    public int maxPathSum(TreeNode root) {
    
        result.add(root.val);

        this.dfs(root);
        return result.get(0);
    }

    private int dfs(TreeNode root) {

        if(root == null) {return 0;}

        int leftMax = this.dfs(root.left), rightMax = this.dfs(root.right);
        leftMax = Math.max(leftMax, 0);
        rightMax = Math.max(rightMax, 0);

        result.set(0, Math.max(result.get(0), root.val + leftMax + rightMax));

        return root.val + Math.max(leftMax, rightMax);
    }
}
