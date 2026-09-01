class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adj = {node: [] for node in range(n)}
        for src, dest in edges:
            adj[src].append(dest)
            adj[dest].append(src)

        visited = set()

        def dfs(node, prev):

            if node in visited:
                return False
            
            visited.add(node)

            for nei in adj[node]:
                if nei == prev:
                    continue
                if not dfs(nei, node):
                    return False

            return True

        if not dfs(0, -1):
            return False
        return len(visited) == n
