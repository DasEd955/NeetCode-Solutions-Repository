class TrieNode {
    private HashMap<Character, TrieNode> children;
    private boolean isWord;

    public TrieNode() {
        this.children = new HashMap<>();
        this.isWord = false;        
    }
}

class WordDictionary {

    private TrieNode root;

    public WordDictionary() {
        this.root = new TrieNode();
    }

    public void addWord(String word) {
        TrieNode node = this.root;
        for(char c : word.toCharArray()) {
            if(!node.children.containsKey(c)) {
                node.children.put(c, new TrieNode());
            }
            node = node.children.get(c);
        }
        node.isWord = true;
    }

    public boolean search(String word) {
        return this.dfs(this.root, 0, word);
    }

    private boolean dfs(TrieNode node, int index, String word) {
        for(int i = index; i < word.length(); i++) {
            char c = word.charAt(i);
            if(c == '.') {
                for(TrieNode child : node.children.values()) {
                    if(this.dfs(child, i + 1, word) == true) {
                        return true;
                    }
                }
                return false;
            }
            else {
                if(!node.children.containsKey(c)) {
                    return false;
                }
                node = node.children.get(c);
            }
        }
        return node.isWord;
    }
}
