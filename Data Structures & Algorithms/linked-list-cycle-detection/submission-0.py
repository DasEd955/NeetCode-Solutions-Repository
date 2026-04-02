# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:

        if not head or head.next == None:
            return False
        
        current = head
        prev = None

        while current:
            if head != current.next and current.next != None:
                current = current.next
            elif head == current.next:
                return True
            current = current.next
            head = head.next
        
        return False
        
        