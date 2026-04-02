# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        current1, current2 = l1, l2
        sumList = ListNode()
        newHead = sumList
        carry = 0
        while current1 or current2:
            if current1 and current2:
                valSum = current1.val + current2.val + carry
            elif current1:
                valSum = current1.val + carry
            else:
                valSum = current2.val + carry
            if valSum > 9:
                sumList.next = ListNode(valSum % 10)
                carry = valSum // 10
            else:
                sumList.next = ListNode(valSum)
                carry = 0
            sumList = sumList.next
            current1, current2 = current1.next if current1 else None, current2.next if current2 else None
        
        if carry != 0:
            sumList.next = ListNode(carry)

        return newHead.next
        