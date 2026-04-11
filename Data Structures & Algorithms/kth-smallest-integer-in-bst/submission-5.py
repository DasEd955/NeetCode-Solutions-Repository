# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        current = root

        while current:
            if not current.left:
                k -= 1
                if k == 0:
                    return current.val
                current = current.right
            else:
                pred = current.left
                while pred.right and pred.right != current:
                    pred = pred.right
                
                if not pred.right:
                    pred.right = current
                    current = current.left
                else:
                    pred.right = None
                    k -= 1
                    if k == 0:
                        return current.val
                    current = current.right
        
        return -1