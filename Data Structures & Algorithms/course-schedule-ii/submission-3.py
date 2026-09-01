class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = {node: [] for node in range(numCourses)}
        for crs, pre_req in prerequisites:
            adj[pre_req].append(crs)

        current_path = set()
        res = []
        def dfs(node):

            if node in current_path:
                return False

            current_path.add(node)

            for nei in adj[node]:
                if not dfs(nei):
                    return False
            adj[node] = []
            current_path.remove(node)
            res.append(node)
            return True

        for node in adj:
            if not dfs(node):
                return []

        res.reverse()
        return res
        


