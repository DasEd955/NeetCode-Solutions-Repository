# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        seenNodes = set()
        current = head

        while current:
            if current in seenNodes:
                return True
            seenNodes.add(current)
            current = current.next
        return False
        