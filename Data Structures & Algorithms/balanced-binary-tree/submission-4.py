# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        return self.maxDepth(root) != -1

    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        maxL = self.maxDepth(root.left)
        if maxL == -1:
            return -1
        
        maxR = self.maxDepth(root.right)
        if maxR == -1:
            return -1
        
        if abs(maxL - maxR) > 1:
            return -1
        
        return 1 + max(maxL, maxR)