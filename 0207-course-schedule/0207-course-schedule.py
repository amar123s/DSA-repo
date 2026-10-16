class Solution:
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        graph={i:[] for i in range(numCourses)}

        for course,prereq in prerequisites:
            graph[prereq].append(course)
        
        visited=set()
        path=set()

        def dfs(course):
            if course in path:
                return False
            if course in visited:
                return True
            visited.add(course)
            path.add(course)

            for neighour in graph[course]:
                if not dfs(neighour):
                    return False
            
            path.remove(course)
            return True

        for course in range(numCourses):
            if not dfs(course):
                return False
        
        return True

        