# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.diameter = 0

        self.maxDepth(root)

        return self.diameter <= 1
    
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        maxL, maxR = self.maxDepth(root.left), self.maxDepth(root.right)    

        self.diameter = max(self.diameter, abs(maxL - maxR))

        return 1 + max(maxL, maxR)