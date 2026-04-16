class MyHashSet {

    private int[] hashSet; 

    public MyHashSet() {
        hashSet = new int[31251];
    }
    
    public void add(int key) {
        hashSet[key / 32] |= this.getMask(key);
    }
    
    public void remove(int key) {
        if(this.contains(key) == true) {
            hashSet[key / 32] ^= this.getMask(key);
        }
    }
    
    public boolean contains(int key) {
        return (hashSet[key / 32] & this.getMask(key)) != 0;
    }

    public int getMask(int key) {
        return 1 << (key % 32);
    }
}

/**
 * Your MyHashSet object will be instantiated and called as such:
 * MyHashSet obj = new MyHashSet();
 * obj.add(key);
 * obj.remove(key);
 * boolean param_3 = obj.contains(key);
 */