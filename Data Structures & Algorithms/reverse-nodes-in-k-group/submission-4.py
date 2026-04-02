# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        current, array = head, list()
        while current:
            array.append(current.val)
            current = current.next
        
        def split(array: list, k: int):
            for i in range(0, len(array), k):
                yield array[i:i+k]
        
        split = list(split(array, k))

        for i in range(len(split)):
            if len(split[i]) == k:
                split[i].reverse()
        
        current = head
        newHead = current
        for i in range(len(split)):
            for j in range(len(split[i])):
                current.next = ListNode(split[i][j])
                current = current.next
        
        return newHead.next
        