from collections import defaultdict

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        adj = defaultdict(set)

        for a, b in edges:
            adj[a].add(b)
            adj[b].add(a)

        
        def dfs(node, visited):

            if node in visited:
                return

            visited.add(node)
            
            for neigh in adj[node]:
                if neigh != node and neigh not in visited:
                    dfs(neigh, visited)

            current.add(node)

            return
            

        
        res = []
        # Delete the edges and check the graph still works. 
        for node_0, node_1 in edges:

            current = set()
            
            # del
            adj[node_0].remove(node_1)
            adj[node_1].remove(node_0)

            # do something
            dfs(node_0, set())

            # if the grap still works, add that edge
            if current == set(adj.keys()):
                res.append([node_0, node_1])

            # re-add
            adj[node_0].add(node_1)
            adj[node_1].add(node_0)

        for idx in range(len(edges) - 1, -1, -1):
            if edges[idx] in res:
                return edges[idx]