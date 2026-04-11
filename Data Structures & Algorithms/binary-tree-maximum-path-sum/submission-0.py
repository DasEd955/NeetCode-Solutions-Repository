# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        
        result = [root.val]

        def dfs(root: Optional[TreeNode]) -> int:

            if not root:
                return 0
            
            leftMax, rightMax = dfs(root.left), dfs(root.right)
            leftMax, rightMax = max(leftMax, 0), max(rightMax, 0)

            result[0] = max(result[0], root.val + leftMax + rightMax)

            return root.val + max(leftMax, rightMax)

        dfs(root)
        return result[0]

        