class Solution {

    private Map<Integer, Integer> visited = new HashMap<>();
    private Map<Integer, ArrayList<Integer>> adj = new HashMap<>();
    private List<Integer> result = new ArrayList<>();

    public int[] findOrder(int numCourses, int[][] prerequisites) {
        for(int[] p : prerequisites) {
            adj.putIfAbsent(p[0], new ArrayList<>());
            adj.get(p[0]).add(p[1]);
        }

        for(int course = 0; course < numCourses; course++) {
            if(dfs(course) == false) {return new int[0];}
        }
        return result.stream().mapToInt(i -> i).toArray();
    }

    private boolean dfs(int course) {
        if(visited.getOrDefault(course, 0) == 1) {return false;}
        if(visited.getOrDefault(course, 0) == 2) {return true;}
        
        visited.put(course, 1);
        for(int neighbor : adj.getOrDefault(course, new ArrayList<>())) {
            if(dfs(neighbor) == false) {return false;}
        }
        result.add(course);
        visited.put(course, 2);
        return true;
    }
}