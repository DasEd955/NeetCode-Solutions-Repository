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

        if not head:
            return None
        
        current, oldToNew = head, dict()
        while current:
            oldToNew[current] = Node(current.val)
            current = current.next
        
        current = head
        while current:
            oldToNew[current].next = oldToNew[current.next] if current.next is not None else None
            oldToNew[current].random = oldToNew[current.random] if current.random is not None else None
            current = current.next
        
        return oldToNew[head]