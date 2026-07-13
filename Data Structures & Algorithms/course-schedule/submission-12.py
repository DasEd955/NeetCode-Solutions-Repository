class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        indegree = [0] * numCourses
        adj = defaultdict(list)
        queue = deque()

        for course, prereq in prerequisites:
            adj[prereq].append(course)
            indegree[course] += 1
        
        for course in range(numCourses):
            if indegree[course] == 0:
                queue.append(course)
        
        finish = 0
        while queue:
            course = queue.popleft()
            finish += 1
            for neighbor in adj[course]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    queue.append(neighbor)
        
        return finish == numCourses 