class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        
        visited, adj = set(), defaultdict(list)

        for edge in edges:
            adj[edge[0]].append(edge[1])
            adj[edge[1]].append(edge[0])
        
        def dfs(node: int) -> None:
            if node in visited:
                return
            visited.add(node)
            for neighbor in adj[node]:
                if not neighbor in visited:
                    dfs(neighbor)
        
        result = 0
        for node in range(n):
            if node not in visited:
                dfs(node)
                result += 1
        
        return result
