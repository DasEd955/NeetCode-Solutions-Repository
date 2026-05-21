# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        
        preIndex, inIndex = 0, 0

        def dfs(limit: Union[int, float]) -> Optional[TreeNode]:
            nonlocal preIndex, inIndex
            if preIndex >= len(preorder):
                return 
            if inorder[inIndex] == limit:
                inIndex += 1
                return

            root = TreeNode(preorder[preIndex])
            preIndex += 1
            root.left = dfs(root.val)
            root.right = dfs(limit) 
            return root
        
        return dfs(float("inf"))
        