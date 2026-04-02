# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    #longest = 0

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        self.longest = 0
        
        self.maxHeight(root)

        return self.longest
        
    def maxHeight(self, root: Optional[TreeNode]) -> int:

        if not root:
            return 0
        
        leftH, rightH = self.maxHeight(root.left), self.maxHeight(root.right)

        self.longest = max(self.longest, leftH + rightH)

        return 1 + max(leftH, rightH)