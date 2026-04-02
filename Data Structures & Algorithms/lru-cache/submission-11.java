public class LRUCache {

    public class Node {
        int key, val;
        Node prev, next;
        public Node(int key, int val) {
            this.key = key;
            this.val = val;
            this.prev = null;
            this.next = null;
        }
    }

    int capacity;
    HashMap<Integer, Node> cache = new HashMap<>();
    Node left, right;

    public LRUCache(int capacity) {
        this.capacity = capacity;
        this.cache = cache;
        this.left = new Node(0, 0);
        this.right = new Node(0, 0);
        this.left.next = this.right;
        this.right.prev = this.left;
    }

    public void remove(Node node) {
        Node prev = node.prev, nxt = node.next;
        prev.next = nxt;
        nxt.prev = prev;
    }

    public void insert(Node node) {
        Node prev = this.right.prev, nxt = this.right;
        prev.next = node;
        nxt.prev = node;
        node.prev = prev;
        node.next = nxt;
    }

    public int get(int key) {
        if(this.cache.containsKey(key)) {
            this.remove(this.cache.get(key));
            this.insert(this.cache.get(key));
            return this.cache.get(key).val;
        }
        return -1;
    }

    public void put(int key, int value) {
        if(this.cache.containsKey(key)) {
            this.remove(this.cache.get(key));
        }
        this.cache.put(key, new Node(key, value));
        this.insert(this.cache.get(key));
        if(this.cache.size() > this.capacity) {
            Node lru = this.left.next;
            this.remove(lru);
            this.cache.remove(lru.key);
        }
    }

}


