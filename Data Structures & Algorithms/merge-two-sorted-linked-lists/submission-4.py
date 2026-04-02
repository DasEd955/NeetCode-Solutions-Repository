# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from typing import Optional
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        if not list1 and not list2:
            return None
        if not list1:
            return list2
        if not list2:
            return list1
        
        current1 = list1
        current2 = list2
        merged = ListNode()
        head = merged

        while current1 and current2:
            if current1.val > current2.val:
                #merged = ListNode(current2.val)
                merged.next = current2
                merged = merged.next
                current2 = current2.next
            else:
                #merged = ListNode(current1.val)
                merged.next = current1
                merged = merged.next
                current1 = current1.next
        
        while current1:
            merged.next = current1
            merged = merged.next
            current1 = current1.next
        
        while current2:
            merged.next = current2
            merged = merged.next
            current2 = current2.next 
    
        return head.next
