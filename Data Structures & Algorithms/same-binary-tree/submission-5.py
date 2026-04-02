# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        Q1, Q2 = deque([p]), deque([q])

        while Q1 and Q2:
            for i in range(len(Q1)):
                nodeP, nodeQ = Q1.popleft(), Q2.popleft()

                if nodeP is None and nodeQ is None:
                    continue
                if nodeP is None or nodeQ is None or nodeP.val != nodeQ.val:
                    return False
                
                Q1.append(nodeP.left)
                Q1.append(nodeP.right)
                Q2.append(nodeQ.left)
                Q2.append(nodeQ.right)
        
        return True