# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None
        
        while len(lists) > 1:
            mergedLists = list()
            for i in range(0, len(lists), 2):    
                l1, l2 = lists[i], lists[i+1] if i+1 < len(lists) else None
                mergedLists.append(self.mergeTwoLists(l1, l2))
            lists = mergedLists
        return lists[0]

    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummyNode = ListNode()
        current = dummyNode
        while l1 and l2:
            if l1.val >= l2.val:
                current.next = ListNode(l2.val)
                l2 = l2.next
            else:
                current.next = ListNode(l1.val)
                l1 = l1.next
            current = current.next
        current.next = l1 or l2
        return dummyNode.next