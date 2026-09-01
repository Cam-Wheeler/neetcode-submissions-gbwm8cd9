class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adj = {node: [] for node in range(n)}
        for src, dest in edges:
            adj[src].append(dest)
            adj[dest].append(src)

        current_path = set()
        visisted = set()

        def dfs(node, prev):

            if node in current_path:
                return False
            
            current_path.add(node)
            visisted.add(node)

            for nei in adj[node]:
                if nei == prev:
                    continue
                if not dfs(nei, node):
                    return False
            adj[node] = []
            current_path.remove(node)

            return True

        if not dfs(0, -1):
            return False
        return len(visisted) == n
