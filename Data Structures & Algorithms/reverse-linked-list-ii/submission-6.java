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
    public ListNode reverseBetween(ListNode head, int left, int right) {
        ListNode dummyNode = new ListNode(0, head), curr = head;

        int i = 1;
        ListNode leftPrev = dummyNode;
        while(i < left) {
            leftPrev = curr;
            curr = curr.next;
            i++;
        }

        ListNode prev = null;
        while(i <= right) {
            ListNode temp = curr.next;
            curr.next = prev;
            prev = curr;
            curr = temp;
            i++;
        }

        leftPrev.next.next = curr;
        leftPrev.next = prev;

        return dummyNode.next;
    }
}