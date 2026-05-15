class Solution {
    public boolean validTree(int n, int[][] edges) {
        if(edges.length > n - 1) {return false;}

        HashSet<Integer> visited = new HashSet<>();
        HashMap<Integer, ArrayList<Integer>> neighbors = new HashMap<>();

        for(int[] edge : edges) {
            neighbors.putIfAbsent(edge[0], new ArrayList<>());
            neighbors.putIfAbsent(edge[1], new ArrayList<>());
            neighbors.get(edge[0]).add(edge[1]);
            neighbors.get(edge[1]).add(edge[0]);
        } 

        return dfs(0, -1, visited, neighbors) && visited.size() == n;
    }

    private boolean dfs(int node, int parent, HashSet<Integer> visited, HashMap<Integer, ArrayList<Integer>> neighbors) {
        if(visited.contains(node)) {return false;}
        visited.add(node);
        for(int neighbor : neighbors.getOrDefault(node, new ArrayList<>())) {
            if(neighbor == parent) {continue;}
            if(dfs(neighbor, node, visited, neighbors) == false) {return false;}
        }
        return true;
    }
}
