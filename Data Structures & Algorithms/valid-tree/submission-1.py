class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) > (n - 1):
            return False
        
        graph = {node: [] for node in range(n)}
        for src, dest in edges:
            graph[src].append(dest)
            graph[dest].append(src)
        
        visited = set()

        def dfs(node, parent):

            if node in visited:
                return False
            
            visited.add(node)
            for neighbour in graph[node]:
                if neighbour == parent:
                    continue
                if not dfs(neighbour, node): return False
            
            return True
        
        return dfs(0, -1) and len(visited) == n