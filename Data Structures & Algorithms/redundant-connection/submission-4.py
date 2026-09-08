from collections import defaultdict

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        adj = defaultdict(list)

        for src, dest in edges:
            adj[src].append(dest)
            adj[dest].append(src)

        visited = set()

        def dfs(node, prev):

            if node in visited:
                return True
            
            visited.add(node)

            for nei in adj[node]:
                if nei == prev:
                    continue
                if dfs(nei, node):
                    return True
            
            visited.remove(node)
            
            return False

        for node in adj:
            if dfs(node, -1):
                for src, dest in reversed(edges):
                    if src in visited and dest in visited:
                        return [src, dest]

        

