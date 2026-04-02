# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

        if not head or not head.next:
            return None
        
        counter, count = head, 0
        while counter:
            count += 1
            counter = counter.next
        middle = count // 2

        left, leftCount = head, 1
        currLeft = left
        while leftCount <= middle:
            leftCount += 1
            left = left.next
        
        right, rightCount = left.next, 0
        currRight = right
        left.next = None
        while right:
            rightCount += 1
            right = right.next 

        prev = None
        while currRight:
            temp = currRight.next
            currRight.next = prev
            prev = currRight
            currRight = temp
        
        start = head
        currLeft = currLeft.next
        while currLeft and prev:
            start.next = prev
            start = start.next
            prev = prev.next
            start.next = currLeft
            start = start.next
            currLeft = currLeft.next

        
        