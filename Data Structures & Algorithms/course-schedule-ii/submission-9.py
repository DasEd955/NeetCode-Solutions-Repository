class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        visited, adj = defaultdict(int), defaultdict(list)
        result = list()

        for p in prerequisites:
            adj[p[0]].append(p[1])
        
        def dfs(course: int) -> bool:
            if visited[course] == 1:
                return False
            if visited[course] == 2:
                return True
            visited[course] = 1
            for neighbor in adj[course]:
                if not dfs(neighbor):
                    return False
            result.append(course)
            visited[course] = 2
            return True
        
        for course in range(numCourses):
            if not dfs(course):
                return []

        return result