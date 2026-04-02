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
    public ListNode removeNthFromEnd(ListNode head, int n) {

        if(head.next == null) {return null;}

        ListNode current = head;
        ArrayList<ListNode> array = new ArrayList<>();
        while(current != null) {
            array.add(current);
            current = current.next;
        }

        Collections.reverse(array);
        array.remove(n-1);
        Collections.reverse(array);

        ListNode newHead = array.get(0);
        newHead.next = null;
        current = newHead;
        for(int i = 1; i < array.size(); i++) {
            current.next = new ListNode(array.get(i).val);
            current = current.next;
        }
        return newHead;
    }
}
