# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:

        if not head or not head.next:
            return False
        
        current = head

        while current and current.next:
            if head != current.next:
                current = current.next
            else:
                return True
            current = current.next
            head = head.next
        
        return False