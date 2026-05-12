"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        
        nodeMap = dict()

        def bfs(node: Optional['Node']) -> Optional['Node']:
            nodeMap[node] = Node(node.val)
            queue = deque([node])

            while queue:
                poppedNode = queue.popleft()
                for neighbor in poppedNode.neighbors:
                    if neighbor not in nodeMap:
                        nodeMap[neighbor] = Node(neighbor.val)
                        queue.append(neighbor)
                    nodeMap[poppedNode].neighbors.append(nodeMap[neighbor])
            
            return nodeMap[node]
        
        return bfs(node)
                
