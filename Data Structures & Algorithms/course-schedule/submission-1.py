from collections import deque, defaultdict

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        # Creating the graph wich will have the pre-requisits.
        graph = defaultdict(list)
        count_pre_requisites = [0] * numCourses

        # Adding the pre-requsits to the graph.
        for course, pre in prerequisites:

            # We're adding the pre-requisits first because we'll be taking them and that will open the courses
            # not the other way around.
            graph[pre].append(course)
            count_pre_requisites[course] += 1

        # Creating the queue of the classes tha tiwll be taken.
        # Adding all the classes with 0 pre_requsits.
        queue = deque([course for course in range(numCourses) if count_pre_requisites[course] == 0])
        taken = 0

        # Taking the classes.
        while queue:

            # Take the course
            course = queue.popleft()
            taken += 1

            # Goign through the classes that this course opens.
            for opened_class in graph[course]:
                count_pre_requisites[opened_class] -= 1
                if count_pre_requisites[opened_class] == 0:
                    queue.append(opened_class)

        return taken == numCourses