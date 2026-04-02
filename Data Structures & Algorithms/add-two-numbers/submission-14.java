/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */

class Solution {
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {

        ListNode c1 = l1, c2 = l2, sumList = new ListNode();
        ListNode newHead = sumList;
        int carry = 0;

        while(c1 != null || c2 != null || carry != 0) {

            int val1 = (c1 != null) ? c1.val : 0, val2 = (c2 != null) ? c2.val : 0;
            int valSum = val1 + val2 + carry;

            sumList.next = new ListNode(valSum % 10);
            carry = (int)valSum / 10;

            sumList = sumList.next;
            c1 = (c1 != null) ? c1.next : null;
            c2 = (c2 != null) ? c2.next : null;

        }
        return newHead.next;
    }
}
