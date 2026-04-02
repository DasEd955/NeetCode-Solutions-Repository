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
    public ListNode reverseList(ListNode head) {

        if(head == null) {
            return head;
        }

        ArrayList<Integer> array = new ArrayList<>();
        while(head != null) {
            array.add(head.val);
            head = head.next;
        }
        Collections.reverse(array);

        ListNode newHead = new ListNode(array.get(0));
        ListNode current = newHead;

        for(int i = 1; i < array.size(); i++) {
            current.next = new ListNode(array.get(i));
            current = current.next;
        }

        return newHead;
    }
        
}

