# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head.next:
            return None
        
        current, array = head, list()
        while current:
            array.append(current)
            current = current.next
        
        array.reverse()
        del array[n-1]
        array.reverse()

        newHead = array[0]
        newHead.next, current = None, newHead
        for node in array[1:]:
            current.next = ListNode(node.val)
            current = current.next
        
        return newHead