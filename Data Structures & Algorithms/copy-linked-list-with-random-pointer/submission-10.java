/*
// Definition for a Node.
class Node {
    int val;
    Node next;
    Node random;

    public Node(int val) {
        this.val = val;
        this.next = null;
        this.random = null;
    }
}
*/

class Solution {
    public Node copyRandomList(Node head) {
        
        if(head == null) {return null;}

        Node current = head;
        HashMap<Node, Node> oldToNew = new HashMap<>();
        while(current != null) {
            oldToNew.put(current, new Node(current.val));
            current = current.next;
        }

        current = head;
        while(current != null) {
            oldToNew.get(current).next = (current.next != null) ? oldToNew.get(current.next) : null;
            oldToNew.get(current).random = (current.random != null) ? oldToNew.get(current.random) : null;
            current = current.next;
        }

        return oldToNew.get(head);
    }
}
