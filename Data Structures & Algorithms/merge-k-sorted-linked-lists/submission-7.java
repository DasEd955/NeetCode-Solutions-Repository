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

public class Solution {

    public ListNode mergeTwoLists(ListNode l1, ListNode l2) {
        ListNode dummyNode = new ListNode();
        ListNode current = dummyNode;
        while(l1 != null && l2 != null) {
            if(l1.val >= l2.val) {
                current.next = new ListNode(l2.val);
                l2 = l2.next;
            }
            else {
                current.next = new ListNode(l1.val);
                l1 = l1.next;
            }
            current = current.next;
        }
        if(l1 != null) {current.next = l1;}
        if(l2 != null) {current.next = l2;}
        return dummyNode.next;
    }

    public ListNode mergeKLists(ListNode[] lists) {
        if(lists == null || lists.length == 0) {return null;}
        while(lists.length > 1) {
            ArrayList<ListNode> mergedLists = new ArrayList<>();
            for(int i = 0; i < lists.length; i += 2) {
                ListNode l1 = lists[i], l2 = ((i+1) < lists.length) ? lists[i+1] : null;
                mergedLists.add(this.mergeTwoLists(l1, l2));
            }
            lists = mergedLists.toArray(new ListNode[0]);
        }
        return lists[0];
    }
}
