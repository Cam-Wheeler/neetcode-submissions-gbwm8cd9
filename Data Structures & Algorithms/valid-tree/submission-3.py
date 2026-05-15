class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        
        graph = {node: [] for node in range(n)}
        for source, dest in edges:
            graph[source].append(dest)
            graph[dest].append(source)
        
        visited = set()

        def dfs(node, prev):

            if node in visited:
                return False
            
            visited.add(node)
            for nei in graph[node]:
                if nei == prev:
                    continue
                
                if not dfs(nei, node):
                    return False
                
            return True
        
        return dfs(0, -1) and len(visited) == n