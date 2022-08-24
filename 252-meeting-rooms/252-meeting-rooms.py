class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        # sort based on start time
        intervals.sort(key = lambda i: i[0])
        
        for i in range(1, len(intervals)):
            i1 = intervals[i - 1]
            i2 = intervals[i]
            
            # if a meeting starts before earlier one ends
            if i1[1] > i2[0]:
                return False
        
        return True