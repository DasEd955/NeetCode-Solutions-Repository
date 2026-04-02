# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if not head:
            return None
        
        previous = None
        current = head

        while current:
            nextTemp = current.next
            current.next = previous
            previous = current
            current = nextTemp
        
        return previous
        