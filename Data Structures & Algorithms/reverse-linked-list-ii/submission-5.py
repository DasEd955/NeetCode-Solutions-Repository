# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummyNode = ListNode(0, head)
        leftPrev, current = dummyNode, head

        i = 1
        while i < left:
            leftPrev, current = current, current.next
            i += 1
        
        prev = None
        while i <= right:
            temp = current.next
            current.next = prev
            prev = current
            current = temp
            i += 1
        
        leftPrev.next.next = current
        leftPrev.next = prev

        return dummyNode.next