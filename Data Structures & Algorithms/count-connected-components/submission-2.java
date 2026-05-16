class Solution {
    public int countComponents(int n, int[][] edges) {

        Set<Integer> visited = new HashSet<>();
        Map<Integer, ArrayList<Integer>> adj = new HashMap<>();

        for(int[] edge : edges) {
            adj.putIfAbsent(edge[1], new ArrayList<>());
            adj.putIfAbsent(edge[0], new ArrayList<>());
            adj.get(edge[0]).add(edge[1]);
            adj.get(edge[1]).add(edge[0]);
        }

        int result = 0;
        for(int node = 0; node < n; node++) {
            if(!visited.contains(node)) {
                dfs(node, visited, adj);
                result++;
            }
        }

        return result;
    }

    private void dfs(int node, Set<Integer> visited, Map<Integer, ArrayList<Integer>> adj) {
        if(visited.contains(node)) {return;}
        visited.add(node);
        for(int neighbor : adj.getOrDefault(node, new ArrayList<>())) {
            if(!visited.contains(neighbor)) {
                dfs(neighbor, visited, adj);
            }
        }
    }
}
