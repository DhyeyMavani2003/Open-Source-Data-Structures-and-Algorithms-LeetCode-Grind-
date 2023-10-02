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
    
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # dfs
        preMap = {i: [] for i in range(numCourses)}

        # map each course to : prereq list
        for crs, pre in prerequisites:
            preMap[crs].append(pre)

        visiting = set()

        def dfs(crs):
            if crs in visiting:
                return False
            if preMap[crs] == []:
                return True

            visiting.add(crs)
            for pre in preMap[crs]:
                if not dfs(pre):
                    return False
            visiting.remove(crs)
            preMap[crs] = []
            return True

        for c in range(numCourses):
            if not dfs(c):
                return False
        return True
