# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    MIN, MAX = float("-inf"), float("inf")

    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        if not root.left and not root.right:
            return True
    
        def dfs(node: Optional[TreeNode], leftVal: float, rightVal: float) -> bool:

            if not node:
                return True
            
            left, right = dfs(node.left, leftVal, node.val), dfs(node.right, node.val, rightVal)

            return left and right and leftVal < node.val < rightVal
        
        return dfs(root, self.MIN, self.MAX)
