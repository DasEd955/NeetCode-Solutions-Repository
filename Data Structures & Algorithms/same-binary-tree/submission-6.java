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
    public boolean isSameTree(TreeNode p, TreeNode q) {

        Deque<TreeNode> Q1 = new LinkedList<>(), Q2 = new LinkedList<>();
        Q1.offer(p);
        Q2.offer(q);

        while(!Q1.isEmpty() && !Q2.isEmpty()) {
            TreeNode nodeP = Q1.poll(), nodeQ = Q2.poll();
            if(nodeP == null && nodeQ == null) {continue;}
            if(nodeP == null || nodeQ == null || nodeP.val != nodeQ.val) {return false;}
            Q1.offer(nodeP.left);
            Q1.offer(nodeP.right);
            Q2.offer(nodeQ.left);
            Q2.offer(nodeQ.right);
        }
        return Q1.isEmpty() && Q2.isEmpty();
    }
}
