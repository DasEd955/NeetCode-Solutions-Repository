class PrefixTree {

    private HashMap<Character, PrefixTree> children;
    private boolean isWord;

    public PrefixTree() {
        this.children = new HashMap<>();
        this.isWord = false;
    }

    public void insert(String word) {
        PrefixTree node = this;
        for(char c : word.toCharArray()) {
            if(!node.children.containsKey(c)) {
                node.children.put(c, new PrefixTree());
            }
            node = node.children.get(c);
        }
        node.isWord = true;
    }

    public boolean search(String word) {
        PrefixTree node = this;
        for(char c : word.toCharArray()) {
            if(!node.children.containsKey(c)) {
                return false;
            }
            node = node.children.get(c);
        }
        return node.isWord;
    }

    public boolean startsWith(String prefix) {
        PrefixTree node = this;
        for(char c : prefix.toCharArray()) {
            if(!node.children.containsKey(c)) {
                return false;
            }
            node = node.children.get(c);
        }
        return true;
    }
}
