# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        #if not p and not q:
            #return True
        #if not p or not q:
            #return False
        
        return self.dfs(p, q)
        
    def dfs(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        if not p and not q:
            return True
        if not p or not q:
            return False
        
        left, right = self.dfs(p.left, q.left), self.dfs(p.right, q.right)

        return p.val == q.val and left and right

        