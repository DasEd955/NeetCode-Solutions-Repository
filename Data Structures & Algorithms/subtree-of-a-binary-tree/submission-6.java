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
    public boolean isSubtree(TreeNode root, TreeNode subRoot) {
        return serialize(root).contains(serialize(subRoot));
    }

    public String serialize(TreeNode node) {
        if(node == null) {return "#";}
        return String.format(".{%d}.{%s}.{%s}", node.val, serialize(node.left), serialize(node.right));
    }
}
