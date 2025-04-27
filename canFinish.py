class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj_list = [[] for _ in range(numCourses)]
        for u, v in prerequisites:
            adj_list[v].append(u)
        
        visited = {i: 0 for i in range(numCourses)}
        sorted_list = []
        def dfs(node):
            if visited[node] == 1:
                return False
            if visited[node] == 2:
                return True
        
            visited[node] = 1
            for neighbor in adj_list[node]:
                if not dfs(neighbor):
                    return False
            
            visited[node] = 2
            sorted_list.append(node)
            return True

        for i in range(numCourses):
            if visited[i] == 0:
                if not dfs(i):
                    return False
        return True
