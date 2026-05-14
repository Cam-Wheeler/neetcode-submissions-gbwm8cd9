class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        graph = {course: [] for course in range(numCourses)}

        for course, prereq in prerequisites:
            graph[course].append(prereq)

        visited = set()

        def dfs(course):

            if course in visited:
                return False
            
            if graph[course] == []:
                return True
            
            visited.add(course)
            for prereq in graph[course]:
                if not dfs(prereq): return False
            
            graph[course] = []
            visited.remove(course)
            return True

        
        for course in range(numCourses):
            if not dfs(course): return False
        
        return True
        
        


