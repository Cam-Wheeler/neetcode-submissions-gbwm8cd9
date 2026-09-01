class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = {n: [] for n in range(numCourses)}
        for course, prereq in prerequisites:
            adj[prereq].append(course)


        current_path = set()
        visited = set()

        def dfs(node):

            if node in current_path:
                return False

            current_path.add(node)

            neighs = adj[node].copy()
            for neigh in neighs:
                res = dfs(neigh)
                if not res:
                    return False
                adj[node].remove(neigh)
            
            current_path.remove(node)

            return True

        for node in adj:
            res = dfs(node)
            if not res:
                return False
        return True

