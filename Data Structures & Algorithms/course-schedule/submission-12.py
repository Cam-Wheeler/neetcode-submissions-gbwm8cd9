class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = {n: [] for n in range(numCourses)}
        for course, prereq in prerequisites:
            adj[prereq].append(course)


        current_path = set()

        def dfs(node):

            if node in current_path:
                return False

            if not adj[node]:
                return True

            current_path.add(node)

            for neigh in adj[node]:
                res = dfs(neigh)
                if not res:
                    return False
            adj[node] = []
            
            current_path.remove(node)

            return True

        for node in adj:
            res = dfs(node)
            if not res:
                return False
        return True

