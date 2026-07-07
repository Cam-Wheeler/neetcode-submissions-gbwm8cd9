class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = {i: [] for i in range(numCourses)}
        for pre_req, course in prerequisites:
            adj[pre_req].append(course) # we are doing it backwards! 


        res = []
        visited = set()
        # topological sort
        def dfs(node, current_path):

            if node in current_path:
                return False

            for neighbour in adj[node]:
                if neighbour not in visited:
                    current_path.add(node)
                    if not dfs(neighbour, current_path):
                        return False
                    current_path.remove(node)
            
            visited.add(node)
            res.append(node)

            return True

        for node in adj:
            if node not in visited:
                if not dfs(node, set()):
                    return []
        return res

        


