from collections import deque, defaultdict

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # prereq -> courses that depend on it; indegree = prerequisites still needed
        graph = defaultdict(list)
        indegree = [0] * numCourses
        for course, prereq in prerequisites:
            graph[prereq].append(course)
            indegree[course] += 1

        # start with every course that has no prerequisites
        q = deque(c for c in range(numCourses) if indegree[c] == 0)
        taken = 0

        while q:
            c = q.popleft()
            taken += 1
            for nxt in graph[c]:
                indegree[nxt] -= 1          # one prerequisite satisfied
                if indegree[nxt] == 0:      # all prerequisites done
                    q.append(nxt)

        return taken == numCourses          # False means a cycle blocked some courses