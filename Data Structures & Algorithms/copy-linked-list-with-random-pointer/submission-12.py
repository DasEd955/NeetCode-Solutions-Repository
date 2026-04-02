"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        
        oldToNew, current = defaultdict(lambda: Node(0)), head
        oldToNew[None] = None

        while current:
            oldToNew[current].val = current.val
            oldToNew[current].next = oldToNew[current.next]
            oldToNew[current].random = oldToNew[current.random]
            current = current.next
        
        return oldToNew[head]
