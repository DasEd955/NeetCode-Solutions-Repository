# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummyNode = ListNode(0, head)
        before, current = dummyNode, head
        i = 1

        while i < left:
            current = current.next
            before = before.next
            i += 1
        
        prev, start = None, current
        while current and i <= right:
            temp = current.next
            current.next = prev
            prev = current
            current = temp
            i += 1
        
        before.next = prev
        start.next = current

        return dummyNode.next