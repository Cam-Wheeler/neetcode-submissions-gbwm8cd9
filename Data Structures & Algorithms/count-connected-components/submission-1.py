class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = {node: [] for node in range(n)}
        for src, dest in edges:
            graph[src].append(dest)
            graph[dest].append(src)

        visited = set()
        con_com = 0

        def dfs(node):
            if node in visited:
                return
            
            visited.add(node)
            for nei in graph[node]:
                dfs(nei)

            return

        for node in graph:
            if node in visited:
                continue
            con_com += 1
            dfs(node)

        return con_com
        