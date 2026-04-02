# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummyNode = ListNode(0, head)
        groupPrev = dummyNode
        while True:
            kth = self.getKth(groupPrev, k)
            if not kth:
                break
            groupNext = kth.next

            current, prev = groupPrev.next, kth.next
            while current != groupNext:
                temp = current.next
                current.next = prev
                prev = current
                current = temp
            
            temp = groupPrev.next
            groupPrev.next = kth
            groupPrev = temp
        
        return dummyNode.next
    
    def getKth(self, current: Optional[ListNode], k: int) -> Optional[ListNode]:
        while current and k > 0:
            current = current.next
            k -= 1
        return current