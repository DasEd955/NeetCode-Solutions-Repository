# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        c1, c2 = l1, l2
        sumList = ListNode()
        newHead = sumList
        
        carry = 0
        while c1 or c2 or carry:
            
            val1 = c1.val if c1 else 0
            val2 = c2.val if c2 else 0
            valSum = val1 + val2 + carry

            sumList.next = ListNode(valSum % 10)
            carry = valSum // 10

            sumList = sumList.next
            c1, c2 = c1.next if c1 else None, c2.next if c2 else None
        
        return newHead.next
        