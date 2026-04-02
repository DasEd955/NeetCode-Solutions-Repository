# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        if not lists or len(lists) == 1 and lists[0] == list():
            return None
        
        array = list()
        for l in lists:
            while l:
                array.append(l.val)
                l = l.next

        array.sort()
        print(array)

        newHead = ListNode()
        current = newHead
        for num in array:
            current.next = ListNode(num)
            current = current.next
        
        return newHead.next