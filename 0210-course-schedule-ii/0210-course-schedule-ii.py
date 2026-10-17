from collections import deque
class Solution:
    def findOrder(self, numCourses: int, prerequisites: list[list[int]]) -> list[int]:
        graph={i:[]for i in range(numCourses)}
        indegree=[0]*numCourses

        for course,prereq in prerequisites:
            graph[prereq].append(course)
            indegree[course]+=1
        
        queue=deque()
        for course in range(numCourses):
            if indegree[course]==0:
                queue.append(course)
        
        order=[]

        while queue:
            course=queue.popleft()
            order.append(course)

            for neighbor in graph[course]:
                indegree[neighbor] -=1

                if indegree[neighbor]==0:
                    queue.append(neighbor)
        
        if len(order)==numCourses:
            return order
        return []
        