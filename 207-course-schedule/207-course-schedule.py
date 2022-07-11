class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        ad_list = {i: set() for i in range(numCourses)}
        for prereq, course in prerequisites:
            ad_list[course].add(prereq)
        
        while len(ad_list) > 0:
            next_course = None
            for course in ad_list:
                if len(ad_list[course]) == 0:
                    next_course = course
                    break
            
            if next_course == None:
                return False

            for course in ad_list:
                ad_list[course].discard(next_course)
            
            ad_list.pop(next_course)
        
        return True