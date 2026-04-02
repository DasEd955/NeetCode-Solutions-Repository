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
    public boolean hasCycle(ListNode head) {

        if(head == null || head.next == null) {return false;}

        ListNode current = head;

        while(current != null && current.next != null) {
            if(current.next != head) {
                current = current.next;
            }
            else {
                return true;
            }
            current = current.next;
            head = head.next;
        }
        return false;
    }
}
