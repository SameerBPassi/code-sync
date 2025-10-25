class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = {i: [] for i in range(numCourses)}
        for a, b in prerequisites:
            graph[b].append(a)
        
        state = [0] * numCourses

        def dfs(node):
            if state[node] == 1:
                return False
            if state[node] == 2:
                return True
            state[node] = 1
            for neigh in graph[node]:
                if not dfs(neigh):
                    return False
            state[node] = 2
            return True
        
        for course in range(numCourses):
            if not dfs(course):
                return False
        return True