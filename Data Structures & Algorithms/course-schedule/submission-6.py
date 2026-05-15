class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        graph = {node: [] for node in range(numCourses)}
        for src, dest in prerequisites:
            graph[src].append(dest)

        
        visited = set()

        def dfs(node):

            if node in visited:
                return False
            
            if graph[node] == []:
                return True
            
            visited.add(node)
            for nei in graph[node]:
                if not dfs(nei): return False
            
            graph[node] = []
            visited.remove(node)

            return True

        for node in graph:
            if not dfs(node): return False
        
        return True