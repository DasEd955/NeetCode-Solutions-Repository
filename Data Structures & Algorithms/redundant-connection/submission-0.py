class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        
        visited, adj = set(), defaultdict(list)

        def dfs(node: int, parent: int) -> bool:
            if node in visited:
                return True
            visited.add(node)
            for neighbor in adj[node]:
                if neighbor == parent:
                    continue
                if dfs(neighbor, node):
                    return True
            return False
        
        for src, dst in edges:
            adj[src].append(dst)
            adj[dst].append(src)
            visited = set()

            if dfs(src, -1):
                return [src, dst]
        
        return []