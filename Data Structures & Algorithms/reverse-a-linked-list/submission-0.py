# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

from typing import Optional

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if not head:
            return None
        
        currentNode = head
        array = list()

        while currentNode:
            array.append(currentNode.val)
            currentNode = currentNode.next
            
        array.reverse()
        print(array)

        newHead = ListNode(array[0])
        current = newHead

        for num in array[1:]:
            current.next = ListNode(num)
            current = current.next
        
        return newHead

        
        

        
        
