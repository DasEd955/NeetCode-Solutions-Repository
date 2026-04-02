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
    public ListNode getKth(ListNode current, int k) {
        while(current != null && k > 0) {
            current = current.next;
            k--;
        }
        return current;
    }
    public ListNode reverseKGroup(ListNode head, int k) {
        ListNode dummyNode = new ListNode(0, head);
        ListNode groupPrev = dummyNode;
        while(true) {
            ListNode kth = this.getKth(groupPrev, k);
            if(kth == null) {break;}
            ListNode groupNext = kth.next;
            ListNode current = groupPrev.next, prev = kth.next;
            while(current != groupNext) {
                ListNode temp = current.next;
                current.next = prev;
                prev = current;
                current = temp;
            }
            ListNode temp = groupPrev.next;
            groupPrev.next = kth;
            groupPrev = temp;
        }
        return dummyNode.next;
    }
}
